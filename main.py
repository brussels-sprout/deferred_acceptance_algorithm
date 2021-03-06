# deferred_acceptance_algorithm
# by brussels_sprout

# main.py combines the interface and the algorithm


from algorithm import algorithm
from interface import intro, input_, output, end


def main():
    women_input, men_input = input_()
    arrangements = algorithm(women_input, men_input)
    output(arrangements)
    end(main)


intro()
main()
