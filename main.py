# deferred_acceptance_algorithm
# by brussels_sprout


from algorithm import algorithm
from interface import input_, output


def main():
    pass


def end():
    if input("\nInput any character(s) to run again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()


main()
end()
