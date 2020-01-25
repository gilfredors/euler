import numpy as np
# Compute sum of multiples of 3 and 5

def is_number_if_multiple_of(number, multiple):
    return number % multiple == 0

def get_number_if_number_is_multiple_of_any(number, multiples):
    for multiple in multiples:
        if is_number_if_multiple_of(number, multiple):
            return number
    return 0

def get_sum_of_multiples_below(number, multiples):
    numbers_below = list(range(1, number))
    multiples = [get_number_if_number_is_multiple_of_any(x, multiples) for x in numbers_below]
    return np.sum(np.array(list(multiples)))


if '__main__' == __name__:
    print(get_sum_of_multiples_below(1000, [3, 5]))