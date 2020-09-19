import math

def prob(n, p, N):
    prob = math.factorial(N) / (math.factorial(n)*math.factorial(N-n)*(2**N))
    return prob

def infoMeasure(N, p):
    entropy_bin = 0
    for i in range(N+1):
        entropy_bin -= prob(i,p,N)*math.log2(prob(i,p,N))
    return entropy_bin

def sumProb(N, p):
    sum = 0
    for i in range(N + 1):
        sum += prob(i,p,N)
    return sum

def approxEntropy(N, p):
    result = 0
    for i in range(N+1):
        result += infoMeasure(i,p)
    return float (result/(N+1))

