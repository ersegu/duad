
def return_prime_numbers(numbers_list):
    new_list = []
    for number in numbers_list:
        if is_prime_number(number):
            new_list.append(number)

    return new_list


def is_prime_number(number):
        if number <= 1:
            return False
        if number == 2 or number == 3 or number == 5:
            return True
        
        if number%2 == 0 or number %3 == 0:
            return False

        counter = 0
        for i in range(5,int(number**0.5)+1):
            if number %i == 0:
                counter += 1
        if counter == 0:
            return True
        else:
            return False


print(return_prime_numbers([5,7,8,11,19,27,34]))



