# deferred_acceptance_algorithm
# by brussels_sprout


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


def create_objects(women_input, men_input):
    # create objects without preferences
    for w in women_input.items():
        Woman(w[0])  # w[0] is only the name (string)

    for m in men_input.items():
        Man(m[0])  # m[0] is only the name (string)

    # set preferences of created objects
    for name, woman in women.items():  # name is woman.name (string)
        woman.set_preferences(women_input[name])

    for name, man in men.items():  # name is man.name (string)
        man.set_preferences(men_input[name])


# test inputs
women_in_test = {"1": ["b", "c", "d", "a"], "2": ["a", "d", "b", "c"], "3": ["c", "b", "d", "a"], "4": ["a", "b", "d", "c"]}
men_in_test = {"a": ["1", "3", "2", "4"], "b": ["4", "3", "1", "2"], "c": ["2", "1", "3", "4"], "d": ["2", "3", "1", "4"]}

algorithm(women_in_test, men_in_test)

# note: woman (variable name) is used for objects and w (variable name) for names of objects (strings)
