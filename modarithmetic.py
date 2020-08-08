# This python program will do some Modular Arithmetic basics. 

from random import randint

# function extGCD
# inputs: two integers x,y
# outputs: three integers: d,s,t such that
#   d = gcd(x,y)
#   sx + ty = d
def extGCD(b, n):
    s,t, u,v = 0,1, 1,0
    while b != 0:
        q, r = n//b, n%b
        m, n = s-u*q, t-v*q
        n,b, s,t, u,v = b,r, u,v, m,n
    gcd = n
    return gcd, s, t
    

# function expMod
# inputs: three integers b,e,n with e >= 0
# output: b^e mod n
# This algorithm must work using the *fast* exponention algorithm described in
# lecture. The slow exponentiation algorithm is in the example file.
def expMod(b,e,n):
	r = 1 
	base = b % n 
	while e > 0:
		if(e % 2 == 1): 
			r = (r * base) % n
		e = e >> 1
		base = (base * base) % n
	return r


# function expModSlow
# inputs: three integers b,e,n with e >= 0
# output: b^e mod n
# This will work, but will take a long time for large e.
# This may be useful for debugging
def expModSlow(b,e,n):
    x = 1
    for i in range(e):
        x *= b
        x %= n
    return x


# function isprime(p,k)
# input: a positive integer p and a positive integer k
# output: true if p is (probably) prime, false otherwise you use use fermat's
# test on p for k iterations. the probability that a we return true for a
# number that isn't actually prime is at most (1/2)^k, unless n is a
# carmichael number, which is also very unlikely.
def isprime(p,k):
    for i in range(k):
    	a = randint(1, p - 1)
    	if(expMod(a, p - 1, p) != 1):
    		return False
    return True
