n = 64
yn = 3

# Euler Method
'''for i in range(0, n):
    ynp = yn + (0.5/n)*(2*yn - yn**2)
    print (i+1, ynp)
    yn = ynp'''

# Modified Euler Method
for i in range(0, n):
    ynap = yn + 0.1*(2*yn - yn**2)
    ynp = yn + 0.05*((2*yn - yn**2) + (2*ynap - ynap**2))
    print (i+1, ynp)
    yn = ynp
