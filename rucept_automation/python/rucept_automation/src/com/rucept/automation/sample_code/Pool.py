import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    1157978484077099,
    10997268995285419, 112272535095293,
    1125827059462171,
    1122725350957293,
    1152800951907373,
    1153797848077099,
    10994726899285419, 112272535095293,
    1125852705942171,
    1122726535095293,
    1152800795190773,
    1157978488077099,
    109972689899285419, 112272535095293,
    1125827059402171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(str(time.time()) + '  %d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()
