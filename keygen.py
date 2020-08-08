# Implement the RSA algorithm in python using the methods in modarithmetic.py

from random import randint
from modarithmetic import *

# function randprime(mn,mx)
# inputs: two integers mn,mx 
# outputs: a random prime between mn and mx
# You should generate random integers over and over using the randint
# method, and test if each one is prime or not.
def randprime(mn,mx):
	a = randint(mn, mx)
	while not isprime(a, 100): 
		a = randint(mn, mx)
	return a 


# function keygen(mn,mx):
# inputs: two integers mn, mx
# outputs: (n,e,d) which are the keys needed for the RSA algorithm. Then
# primes used should be different and between the ranges mn and mx.
# Keep in mind that e and d must BOTH BE POSITIVE.
def keygen(mn,mx):
	p = randprime(mn, mx)
	q = randprime(mn, mx)
	while p == q: 
		q = randprime(nm, mx) 
	n = p * q
	phi = (p - 1) * (q - 1) 
	e = randint(1, p)
	while extGCD(e, phi)[0] != 1: 
		e = randint(3, p)
	return n, e, (extGCD(e, phi)[1] % phi)


