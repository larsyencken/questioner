# -*- coding: utf-8 -*-
#
#  cli.py
#  questioner
#

"""
A command-line client for annotating things.
"""

import re
import os
from typing import List, Set, Optional

import readchar
import blessings


SKIP_KEY = '\r'
SKIP_LINE = ''
QUIT_KEY = 'q'
QUIT_LINE = 'q'
EMAIL_REGEX = '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,6}$'


class QuestionSkipped(Exception):
    pass


class QuitCli(Exception):
    pass


class Cli:
    def __init__(self,
                 skip_key=SKIP_KEY,
                 skip_line=SKIP_LINE,
                 quit_key=QUIT_KEY,
                 quit_line=QUIT_LINE):
        self.skip_key = skip_key
        self.skip_line = skip_line
        self.quit_key = quit_key
        self.quit_line = quit_line

        self.terminal = blessings.Terminal()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def yes_or_no(self, prompt, newline=True):
        v = self.input_bool(prompt)

        if newline:
            print()

        return v

    def underline(self, s):
        return self.terminal.underline(str(s))

    def choose_one(self, prompt, options):
        print(prompt)

        if len(options) < 10:
            for i, option in enumerate(options):
                print('  {}. {}'.format(self.underline(i), option))

            ix = self.input_number_quick(0, len(options) - 1)

        else:
            for i, option in enumerate(options):
                print(f'  {i}. {option}')

            ix = self.input_number(0, len(options) - 1)

        print()
        return options[ix]

    def choose_many(self, prompt, options):
        print(prompt)
        vs = set([o for o in options
                  if self.yes_or_no(f'  {o}', newline=False)])
        print()
        return vs

    def give_an_int(self, prompt, minimum=None, maximum=None):
        print(prompt)

        is_digit_range = (minimum is not None
                          and maximum is not None
                          and (0 <= minimum <= maximum <= 9))
        if is_digit_range:
            v = self.input_number_quick(minimum, maximum)

        else:
            v = self.input_number(minimum, maximum)

        print()
        return v

    def read_char(self):
        c = readchar.readchar()

        if c == self.skip_key:
            raise QuestionSkipped()

        elif c == self.quit_key:
            raise QuitCli()

        print(c, end='', flush=True)

        return c

    def read_line(self, prompt):
        line = input(prompt).rstrip('\n')

        if line == self.skip_line:
            raise QuestionSkipped()

        elif line == self.quit_line:
            raise QuitCli()

    def input_bool(self, query: str) -> bool:
        print('{}? ({}/{})'.format(query,
                                   self.underline('y'),
                                   self.underline('n')),
              end=' ', flush=True)

        while True:
            c = self.read_char()
            print()
            if c in ('y', 'n'):
                break

            print('ERROR: please press y, n, or return')

        return c == 'y'

    def input_number(self,
                     query: str,
                     minimum: Optional[int] = None,
                     maximum: Optional[int] = None) -> int:
        number_query = query + '> '
        while True:
            r = self.read_line(number_query)
            try:
                v = int(r)
                if ((minimum is None or minimum <= v)
                        and (maximum is None or maximum >= v)):
                    return v
                else:
                    print('ERROR: invalid number provided')

            except ValueError:
                print('ERROR: please enter a number')

    def input_number_quick(self,
                           minimum: Optional[int] = None,
                           maximum: Optional[int] = None) -> int:
        assert minimum >= 0 and maximum <= 9

        while True:
            r = self.read_char()
            print()
            try:
                v = int(r)
                if ((minimum is None or minimum <= v)
                        and (maximum is None or maximum >= v)):
                    return v
                else:
                    print('ERROR: invalid number provided')

            except ValueError:
                print('ERROR: please enter a number')

    def input_multi_options(self, title: str, options: List[str]) -> Set[str]:
        print(title)
        selected = set([o for o in options if self.input_bool('  ' + o)])
        return selected

    def input_single_option(self, title: str, options: List[str]) -> str:
        print(title)
        for i, o in enumerate(options):
            print('  {0}. {1}'.format(i + 1, o))

        v = self.input_number('pick one', minimum=1, maximum=len(options))

        return options[v - 1]

    def input_email(self) -> str:
        while True:
            v = self.read_line('email address> ')
            if re.match(EMAIL_REGEX, v, re.IGNORECASE):
                return v

            print('ERROR: please enter a valid email address')

    def input_string(query: str, allow_empty: bool = False) -> str:
        while True:
            v = input(query + '> ').strip()
            if allow_empty or v:
                return v

            print('ERROR: cannot be left empty')

    def pause(message: str = 'Press any key to continue...') -> None:
        readchar.readchar()

    def clear_screen() -> None:
        os.system('clear')
