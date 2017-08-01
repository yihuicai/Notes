def number_needed(a, b):
    '''
    This function takes in strings and output number of characters
    to be deleted in order to make it an anagram
    '''
    a_sorted=sorted(a)
    b_sorted=sorted(b)
    ndel=0
    i=0
    j=0
    while i != len(a) and j !=len(b):
        if a_sorted[i]>b_sorted[j]:
            j += 1
            ndel += 1
        elif a_sorted[i]==b_sorted[j]:
            i += 1
            j += 1
        else:
            i += 1
            ndel += 1
    if i != len(a):
        ndel += len(a)-i
        
    elif j != len(b):
        ndel += len(b)-j
    return ndel


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
