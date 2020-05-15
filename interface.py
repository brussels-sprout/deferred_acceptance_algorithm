# deferred_acceptance_algorithm
# by brussels_sprout


# interface.py contains the interface code


def intro():
    title()
    info()


def title():
    print("\033[1m" + "Deferred Acceptance Algorithm" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def info():
    print("Information:")
    print(" • For an explanation of the algorithm and the problem watch https://youtu.be/Qcv1IqHWAzg by Numberphile.")
    print(" • The notations used (\"woman\" and \"man\") are according the the Numberphile video.")
    print(" • So, in this program, the women \"propose\" to the men.")
    print(" • Note that the inputs and output are case sensitive.")
    print(" • Also note that this program currently only solves the problem for two sets of elements of equal size.")


def input_():
    pass


def output():
    pass


def end(main):  # main is function to run again
    if input("\nInput any character(s) to run again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()
