'''
Input :
- AA : attribute affinity matrix

Output :
- CA : clustered affinity matrix

'''

n = 3
AA = [1,1,1] # imagine it's a n*n matrix
index = 3
CA = [0,0,0]

CA[1] = AA[1]
CA[2] = AA[2]

while index<= n:
    for i in range(1, index-1):
        loc = 1 #'placement given by maximum cont value'
        for j in range(index, loc):
            CA[j] = CA[j-1]
        CA[loc] = AA[index]
        index = index -1
# Order the rows according to the relative ordering of columns