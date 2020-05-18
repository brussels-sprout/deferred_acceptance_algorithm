# deferred_acceptance_algorithm
# by brussels_sprout


# interface.py contains the interface code


def intro():
    title()
    info()
    example()


def title():
    print("\033[1m" + "Deferred Acceptance Algorithm" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def info():
    print("Information:")
    print(" • For an explanation of the algorithm and the problem watch https://youtu.be/Qcv1IqHWAzg by Numberphile.")
    print(" • The members of group A \"propose\" to the members of group B.")
    print(" • Note that the inputs and output are case sensitive.")
    print(" • Also note that this program currently only solves the problem for two sets of elements of equal size.\n")


def example():
    print("Example inputs:")
    print(" • Names: Olivia, Willow, Sarah (separated by a comma and a space (\", \"))")
    print(" • Preferences: Harry, Charlie, Harry (separated by a comma and a space (\", \") and in descending order of preference (first is the most preferable))")


def input_():
    print("\n-----Input-----")

    women_dict = {}
    women_names = extractor(input(f"\nInput the names of group A's members: "))
    print()  # empty line
    for name in women_names:
        preferences = extractor(input(f"Input {name}'s preferences: "))
        women_dict.update({name: preferences})

    men_dict = {}
    men_names = extractor(input(f"\nInput the names of group B's members: "))
    print()  # empty line
    for name in men_names:
        preferences = extractor(input(f"Input {name}'s preferences: "))
        men_dict.update({name: preferences})

    if not check_sizes(women_dict, men_dict):
        invalid_input(input_)

    if not check_preferences_content(women_dict, men_dict):
        invalid_input(input_)


def extractor(string):
    return string.split(", ")


def invalid_input(func):  # func is function to run again
    print("\nInvalid input. Please try again.")
    func()


def check_sizes(group_a, group_b):
    return check_groups_size(group_a, group_b) and check_preferences_size(group_a, group_b)


def check_groups_size(group_a, group_b):  # checks if the two groups have equal size
    if len(group_a) == len(group_b):
        return True
    else:
        return False


def check_preferences_size(group_a, group_b):  # checks if the preferences of each group are the same size as the other group
    for preferences in group_a.values():
        if not len(preferences) == len(group_b):
            return False

    for preferences in group_b.values():
        if not len(preferences) == len(group_a):
            return False

    return True


def check_preferences_content(group_a, group_b):  # # checks if the preferences of each group only contain the names of the other group
    for preferences in group_a.values():
        for preference in preferences:
            if preference not in group_b.keys():
                return False

    for preferences in group_b.values():
        for preference in preferences:
            if preference not in group_a.keys():
                return False

    return True


def output():
    pass


def end(func):  # func is function to run again
    if input("\nInput any character(s) to run again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        func()
