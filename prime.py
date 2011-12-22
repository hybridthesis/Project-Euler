import math
from math_func import *

class Prime:


    def __init__(self, **kargs):
        self.primes = []
        try:
            self.n_max = kargs['max']
            self.numlist = range(2, self.n_max)
            self._createPrime()
        except Exception as ex:
            print ex
            print "No max found! Please provide."
        try:
            self.nth = kargs['nth']
            self._getNth()
        except:
            pass

    def _createPrime(self):
        while len(self.numlist):
            current_prime = self.numlist[0]
            d = lambda x: x% current_prime
            self.numlist = filter(d,self.numlist)
            self.primes.append(current_prime)


    def _getNth(self):
        """Search for the nth prime number"""
        nth = self.nth

        t = lambda n: n/math.log(n)

        i = 2
        while t(i)<nth:
            i = i + 1

        self.numlist = range(2, i)
        self._createPrime()
        self.nth = self.primes[nth-1]
    def __iter__(self):
        pass
