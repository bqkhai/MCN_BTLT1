
def prob(n, p):
    return float(p*pow(1-p,n-1))

def infoMeasure(n, p):
    entropy_geo = 0
    for i in range(1,n+1):
        entropy_geo += i/(2**i)
    return float (entropy_geo)

def sumProb(N, p):
    result = 0
    for i in range(1,N+1):
        result += prob(i,p)
    return float (result)
'''
P(x ≤ N) = P(x = 1) + P(x = 2)· · · P(x = N)
         = p + p*(1-p) + p*(1-p)^2 + ... + p*(1-p)^(N-1)    - cấp số nhân 
         = p*[1-(1-p)^N]/[1-(1-p)]
         = 1 - (1-p)^N 
         ~ 1
'''

def approxEntropy(N, p):
    result = 0
    for i in range(1,N+1):
        result += infoMeasure(i,p)
    return float (result/N)
'''
trung bình lượng tin:
    H(x) = (H(1) + H(2) + ... + H(N)) / N
         = i/(2^i * N) (với i chạy từ 1 đến N)
         ~ i/(2^i) khi i tiến ra vô cùng
    H(p=0.5) = (-0.5*log(0.5)-0.5log(0.5)) / 0.5 = 2
'''
