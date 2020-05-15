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


def separator():
    print("\n-------------------------")


def input_():
    separator()

    print("Group A:")
    women_inter = input("   Input the names of group A's members: ")  # inter for intermediate

    separator()


def output():
    pass


def end(main):  # main is function to run again
    if input("\nInput any character(s) to run again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()
