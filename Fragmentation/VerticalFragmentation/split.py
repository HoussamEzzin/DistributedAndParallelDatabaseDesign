'''

input : CA clustered affinity matrix 
R relation
ref attribute usage matrix
acc access frequency matrix

output : F set of fragements
'''

z = 0
n = 3 # we suppose n = 3
CT = [0,0,0]
CB = [1,0,1]
CO = [1,1,1]
CTQ = [0,1,1]
CBQ = [1,0,0]
COQ = [0,0,0]
# the sbscripts in the cost equations indicate the split point
CTQ[n-1] = CT[0]
CBQ[n-1] = CB[0]
COQ[n-1] = CO[0]
best = CTQ[n-1]*CBQ[n-1] - (COQ[n-1])**2

shift = False

while shift == False:
    for i in range(n-2,1,-1):
        CTQ[i] = CT[n]
        CBQ[i] = CB[n]
        COQ[i] = CO[n]
        z = CTQ[i]*CBQ[i] - (COQ[i])**2
        if z > best :
            best = z
    shift = True

# Reconstruct the matrix according to the shift position
TAR = []
BAR = []
K = ''
R1 = TAR.append(K)
R2 = BAR.append(K)
F = R1 + R2

 