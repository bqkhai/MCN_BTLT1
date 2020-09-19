import math

def prob(n, p, r):
    prob = math.factorial(n+r-1) / (math.factorial(n)*math.factorial(r-1)*(2**n))
    return prob

def infoMeasure(N, p, r):
    entropy_negbin = 0
    for i in range(N+1):
       entropy_negbin += prob(i,p,r)*math.log2(prob(i,p,r))
    return entropy_negbin

def sumProb(N, p, r):
    sum = 0
    for i in range(N + 1):
        sum += prob(i,p,r)
        return sum

def approxEntropy(N, p, r):
    result = 0
    for i in range(N+1):
        result += infoMeasure(i,p,r)
    return float (result/N)


