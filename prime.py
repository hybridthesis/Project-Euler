import math

class Prime:
    def __init__(self, **args):
        self.value = 0
        self.currentvalue = 3
        self.primelist = [2, 3]
        try:
            self.operation = args.keys()[0]
        except:
            print "Warning: No operation given!"
            self.operation = 'none'
        return 

    def __iter__(self):
        return self

    def next(self):
        primeCandidate = self.currentvalue + 2
        primeTestMax = int(math.sqrt(primeCandidate))+1

        def primetest(pCandidate):
            for i in self.primelist:
                if i>primeTestMax: return True
                if pCandidate % i == 0 : return False
            return True
        
        while not primetest(primeCandidate):
            primeCandidate +=2

        #Congratulations! You have found your prime number =)
        self.currentvalue = primeCandidate
        self.primelist.append(primeCandidate)
        return primeCandidate


    def __repr__(self):
        return str(self.value)
