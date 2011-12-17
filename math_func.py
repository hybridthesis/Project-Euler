def getNextPrime(self, prime):
    if self.isPrime(prime): prime = prime + 1

    while not self.isPrime(prime):
        prime = prime + 1

    return prime

def lcm(self, *args):

    if type(args[0]) is type(list()):
        args = args[0]

    num = list(args)

    prime_factors = []

    prime = 2
    previous_list = num
    while len(num) is not 0:
        previous_size = len(num)
        previous_list = num
        num = map(lambda x: self.divides(prime, x) and x/prime or x, num)
        num = filter(lambda x: x != 1, num)

        if previous_size != len(num) or previous_list != num:
            prime_factors.append(prime)
        else:
            prime = self.getNextPrime(prime)

    return reduce(lambda x, y: x * y, prime_factors)


def divides(self, *args):
    "Check if divisor divides dividend"

    if type(args[0]) is type(list()):
        args = args[0]

    dividend = args[-1]
    for item in args:
        if (dividend % item): return 0

    return 1

def even(self, input_z):
    "Check if is even"
    if input_z % 2: return 0
    else: return 1


def factorization(self, input_z):
    "Provides function for factorization"

    lower = [1]
    upper = [input_z]
    divisor = 2
    dividend = input_z
    while divisor < dividend:
        if self.divides(divisor, input_z):
            lower.append(divisor)
            dividend = input_z/divisor
            if divisor != dividend:
                upper.append(dividend)
        divisor += 1

    upper.reverse()

    return lower + upper


def isPrime(self, input_z):
    "Returns numbers of factors if"

    factors = self.factorization(input_z)

    if len(factors) > 2: return 0
    else: return 1


def gcd(self, input_a, input_b):
    "Returns the greatest common factor"

    factors_of_a = self.factorization(input_a)
    factors_of_b = self.factorization(input_b)

    if(factors_of_a[-1] < factors_of_b[-1]):
        try_input = input_b
        try_factors = factors_of_a
    else:
        try_input = input_a
        try_factors = factors_of_b

    try_factors.reverse()

    for item in try_factors:
        if self.divides(item, try_input):
            return item
