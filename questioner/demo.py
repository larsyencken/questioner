from .cli import Cli


def demo():
    with Cli() as c:
        c.yes_or_no('Are you hurt')

        c.choose_many(
            'What symptoms do you have?',
            ['pain', 'nausea', 'anxiety'],
        )

        c.give_an_int(
            'How would you rate this experience (1-5)', 1, 5
        )

        c.choose_one('Which do you like best', ['dogs', 'cats', 'horses'])


if __name__ == '__main__':
    demo()
