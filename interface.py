# deferred_acceptance_algorithm
# by brussels_sprout


def intro():
    title()


def title():
    print("\033[1m" + "Deferred Acceptance Algorithm" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


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
