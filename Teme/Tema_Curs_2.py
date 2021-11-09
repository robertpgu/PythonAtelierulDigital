def ascending_sort(numbers):
    numbers.sort()
    return numbers



def descending_sort(numbers):
    numbers.sort(reverse=True)
    return numbers


def even_numbers(numbers):
    ascending_sort(numbers)
    numbers[::2]
    return numbers


def odd_numbers(numbers):
    ascending_sort(numbers)
    odds = numbers[1::2]
    return odds


def multiples_of_3(numbers):
    for i in numbers:
        if numbers[i] % 3 != 0:
            numbers.pop(i)
    return numbers

if __name__ == '__main__':

    numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
    # ascending_sort(numbers)
    # descending_sort(numbers)
    # odd_numbers(numbers)
    # even_numbers(numbers)
    # multiples_of_3(numbers)
    print(numbers)