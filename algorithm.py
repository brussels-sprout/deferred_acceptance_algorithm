# deferred_acceptance_algorithm
# by brussels_sprout

# algorithm.py contains the pure algorithm

# Regarding the notation ("woman" and "man") used in the code, it is according to
# the Numberphile video (https://youtu.be/Qcv1IqHWAzg) on this problem.


from elements import *


# dict (dictionary) contains names (string) as keys and preferences (list where smaller index is higher preference) as values
def algorithm(women_input, men_input):
    create_objects(women_input, men_input)

    not_finished = True

    while not_finished:
        if False in [woman.is_engaged for woman in women.values()]:  # if not all women are engaged
            for woman in women.values():
                if not woman.is_engaged:
                    woman.propose(woman.preferences[0])
        else:
            not_finished = False

    arrangements_with_objects = {}  # {woman: man, ...} (format; woman and man are objects)

    for woman in women.values():
        arrangements_with_objects.update({woman: woman.engaged_with})

    arrangements_with_names = objects_to_names(arrangements_with_objects)

    return arrangements_with_names


def create_objects(women_input, men_input):
    # create objects without preferences
    for w in women_input.keys():
        Woman(w)  # w is just the woman's name

    for m in men_input.keys():
        Man(m)  # m is just the man's name

    # set preferences of created objects
    for name, woman in women.items():  # name is woman.name (string)
        woman.set_preferences(women_input[name])

    for name, man in men.items():  # name is man.name (string)
        man.set_preferences(men_input[name])


def objects_to_names(arrangements_with_objects):  # replaces objects in arrangements_with_objects with their names
    arrangements_with_names = {}

    for arrangement in arrangements_with_objects.items():
        woman, man = arrangement
        arrangements_with_names.update({woman.name: man.name})

    return arrangements_with_names


# Example inputs and output:
# women_in_test = {"1": ["b", "c", "d", "a"], "2": ["a", "d", "b", "c"], "3": ["c", "b", "d", "a"], "4": ["a", "b", "d", "c"]}
# men_in_test = {"a": ["1", "3", "2", "4"], "b": ["4", "3", "1", "2"], "c": ["2", "1", "3", "4"], "d": ["2", "3", "1", "4"]}
#
# print(algorithm(women_in_test, men_in_test))
