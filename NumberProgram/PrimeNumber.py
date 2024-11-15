def is_prime(num):
    if num <= 1:
        return False

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False

    return True

print(is_prime(11))  # Output: True
print(is_prime(15))  # Output: False
print(is_prime(2))   # Output: True
print(is_prime(1))   # Output: False
