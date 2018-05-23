# Check the number for prime
def check_prime(number):
    if number % 2 == 0:  # All even numbers are composite (except 2)
        return number == 2
    else:
        for i in range(3, number, 2):  # Search for odd multipliers
            if number % i == 0:
                return False
        return True


# Search for prime multipliers
def factorization(number):
    multipliers = []
    while number % 2 == 0:  # Search for even prime divisors
        number //= 2
        multipliers.append(2)
        if number == 1:
            return multipliers
    if number == 3:
        multipliers.append(3)
        return multipliers
    for i in range(3, number+1, 2):  # Search for odd prime divisors
        if check_prime(i):
            while number % i == 0:
                number //= i
                multipliers.append(i)
                if number == 1:
                    return multipliers


# Check input and generate a line with the result
def check_number(number):
    if number.isdigit():
        number = int(number)
        if number > 1:
            if check_prime(number):
                return 'Число ' + str(number) + ' — простое'
            else:
                # Generate a line type "6=2*3"
                return str(number) + '=' + '*'.join([str(i) for i in factorization(number)])
        else:
            return 'Введите натуральное число больше 1'
    else:
        return 'Введите натуральное число больше 1'
