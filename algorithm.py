# deferred_acceptance_algorithm
# by brussels_sprout


from Woman import Woman
from Man import Man


# dict (dictionary) contains names (string) as keys and preferences (list where smaller index is higher preference) as values
def algorithm(women_dict, men_dict):
    create_objects(women_dict, men_dict)

    women = Woman.collection
    men = Man.collection

    not_finished = True

    while not_finished:
        if False in [w.is_engaged for w in women]:  # if not all women are engaged
            for w in women.values():
                if not w.is_engaged and len(w.preferences) != 0:
                    w.propose(w.preferces[0])
        else:
            not_finished = False


def create_objects(women_dict, men_dict):
    for w in women_dict.items():
        Woman(*w)

    for m in men_dict.items():
        Man(*m)

