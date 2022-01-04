#input : R relation, Pr: set of simple predicates
#output : Pr2 : set of simple predicates

F = [] # set of minterm fragments

Pr2 = []

# find pi belongs to Pr such that pi partitions R according to Rule 1
pi= ''
fi = pi +' f'
Pr = [pi]
Pr2.append(Pr)
Pr.remove(pi)
F.append(fi)
while len(Pr2) == 0:
    pj = ''
    fj = pj +'f'
    '''
    Find pj that belongs to Pr such that pj partitions some
    fk of Pr2 according to Rule 1
    '''
    Pr=[pj]
    Pr2.append(pj)
    Pr.remove(pj)
    F.append(fj)
    pk = ''
    fk = pk +''
    if pk in Pr2 :
        Pr2.remove(pk)
        F.remove(fk)
    