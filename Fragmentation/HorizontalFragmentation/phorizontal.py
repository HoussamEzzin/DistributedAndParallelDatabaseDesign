'''
Input : 
- R : RELATION
- Pr : SET OF SIMPLE PREDICATES

Ouput :
- Fr : set of horizontal fragements of R

'''

import com_min

Pr = []
R = 'relation'

Pr2 = com_min(R,Pr)
#determine the set M of minterm predicates
#determine the set I of implications among pi that belong to Pr2
mi = 'minterm predicate'
M = [mi]
I = []
for mi in M:
    if mi not in I:
        M.append(mi)
sigma = 1
Ri = sigma*R
Fr = [Ri]
        
