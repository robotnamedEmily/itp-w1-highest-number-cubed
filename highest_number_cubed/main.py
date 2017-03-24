"""This is the entry point of the program."""


def highest_number_cubed(limit):
    num_list = []
    num = 0
    while num < limit:
        if num ** 3 < limit:
            num_list.append(num)
        num += 1
    return max(num_list)
            
            