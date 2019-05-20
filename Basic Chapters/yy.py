def is_prime(num):
    if num in range(0, 2):
        return False
    else:
        c = 0
        for i in range(1, num+1):
            if num % i == 0:
                c += 1
        return False if c > 2 else True


print(is_prime(5))

