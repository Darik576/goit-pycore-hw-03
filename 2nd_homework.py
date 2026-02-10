import random


def get_numbers_ticket(min_number, max_number, quantity):
    if min_number < 1 or max_number > 1000:
        return []

    if quantity > (max_number - min_number + 1):
        return []

    numbers = []

    while len(numbers) < quantity:
        number = random.randint(min_number, max_number)

        if number not in numbers:
            numbers.append(number)

    numbers.sort()
    return numbers


if __name__ == "__main__":
    ticket = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", ticket)
