"""
Junk 2
"""


class Thing(object):
    THING_VAR1 = "Doggy"

    def __init__(self):
        pass

    def get_thing_var(self):
        global THING_VAR1
        return THING_VAR1


def main():
    thing = Thing()

    print(thing.get_thing_var())


if __name__ == '__main__':
    main()