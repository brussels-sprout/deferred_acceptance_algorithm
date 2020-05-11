# deferred_acceptance_algorithm
# by brussels_sprout


from elements import *


# dict (dictionary) contains names (string) as keys and preferences (list where smaller index is higher preference) as values
def algorithm(women_dict, men_dict):
    create_objects(women_dict, men_dict)

    print(women)
    print(men)

    not_finished = True

    while not_finished:
        if False in [w.is_engaged for w in women.values()]:  # if not all women are engaged
            for w in women.values():
                if not w.is_engaged and len(w.preferences) != 0:
                    w.propose(w.preferences[0])
        else:
            not_finished = False


def create_objects(women_dict, men_dict):
    for i in range(2):
        for w in women_dict.items():
            Woman(*w)

        for m in men_dict.items():
            Man(*m)


women_dict_ = {"1": ["b", "c", "d", "a"], "2": ["a", "d", "b", "c"], "3": ["c", "b", "d", "a"], "4": ["a", "b", "d", "c"]}
men_dict_ = {"a": ["1", "3", "2", "4"], "b": ["4", "3", "1", "2"], "c": ["2", "1", "3", "4"], "d": ["2", "3", "1", "4"]}

algorithm(women_dict_, men_dict_)
