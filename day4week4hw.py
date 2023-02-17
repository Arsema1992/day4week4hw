def boolean_to_string(b):
    #o(n) => liner
    return 'True' if b else 'False'

def invert(lst):
     #o(n) => liner
    return [-x for x in lst]


def in_array(a1, a2):
    r = []
    #o(n)
    for s1 in a1:
        #o(n)
        for s2 in a2:
            #n(1)
            if s1 in s2 and s1 not in r:
                r.append(s1)
    return sorted(r)
#o(n^2)
