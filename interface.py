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

    women_dict = {}
    women_names = extractor(input(f"Input the names of group A's members: "))
    for name in women_names:
        preferences = extractor(input(f"\nInput {name}'s preferences: "))
        women_dict.update({name: preferences})

    men_dict = {}
    men_names = extractor(input(f"Input the names of group B's members: "))
    for name in men_names:
        preferences = extractor(input(f"\nInput {name}'s preferences: "))
        men_dict.update({name: preferences})


def extractor(string):
    return string.split(", ")


def output():
    pass


def end(main):  # main is function to run again
    if input("\nInput any character(s) to run again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()
