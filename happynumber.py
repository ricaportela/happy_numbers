def sum_of_squares(number):
    digits = [int(char) ** 2 for char in str(number)]
    return sum(digits)


def happy(number):
    box = []              
    n = number
    if number < 0:
        return True

    while True and n not in box:     
        box.append(n)
        n = sum_of_squares(n)
    
        return n == 1


