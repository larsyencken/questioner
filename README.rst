==========
Questioner
==========


.. image:: https://img.shields.io/pypi/v/questioner.svg
        :target: https://pypi.python.org/pypi/questioner

.. image:: https://img.shields.io/travis/larsyencken/questioner.svg
        :target: https://travis-ci.org/larsyencken/questioner

.. image:: https://readthedocs.org/projects/questioner/badge/?version=latest
        :target: https://questioner.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


A human-friendly Python library for asking people questions on the command-line.

Motivation
----------

Data often needs a human eye. I found myself writing over and over the code to help me investigate data manually on the command-line; ``questioner`` is my attempt to make this tool the right way once.

It's suitable for:

- **Labelling data manually** faster than you can in excel spreadsheets or similar setups
- **Active learning loops** where you and a machine-learnining agent collaborate, reducing the need for training data
- **Short question-based UIs** on the command-line where you need a user's input to continue

Usage
-----

Python API
~~~~~~~~~~~

You write a simple Python api that asks you things.

.. code-block:: python

    import questioner

    with questioner.Cli() as c:
        is_hurt = c.yes_or_no('Are you hurt')

        symptom_set = c.choose_many(
            'What symptoms do you have?',
            ['pain', 'nausea', 'anxiety'],
        )

        rating = c.give_an_int(
            'How would you rate this experience (1-5)', 1, 5
        )

        choice = c.choose_one('Which do you like best',
                              ['dogs', 'cats', 'horses'])


On the terminal
~~~~~~~~~~~~~~~

When run, the experience on the terminal looks like the following:

.. code-block::

    $ python -m questioner.demo
    Are you hurt? (y/n) n

    What symptoms do you have?
      pain? (y/n) y
      nausea? (y/n) n
      anxiety? (y/n) n

    How would you rate this experience (1-5)
    3

    Which do you like best
      0. dogs
      1. cats
      2. horses
    1

The user can by default skip a question (raising ``QuestionSkipped``) by pressing enter, or quit the entire cli by pressing ``q`` (raising ``QuitCli``).


Features
--------

* Support for boolean, numeric, single-choice and multiple-choice questions
* Uses single-keystroke input where possible

License
-------

MIT licensed.
