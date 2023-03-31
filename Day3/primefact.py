def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    if is_prime(n):
        return n
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

def sum_of_largest_prime_factors(n):
    result = 0
    for i in range(n, n+9):
        result += largest_prime_factor(i)
    return result

print(sum_of_largest_prime_factors(10))
