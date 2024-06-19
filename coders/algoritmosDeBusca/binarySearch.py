def naive_search(l, target):
    for i in range(len(l)):
        if l[i]==target:
            return i
        
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low=0
    if high is None:
        high=len(l)-1

    midpoint=(low+high)//2

    if l[midpoint]==target:
        return midpoint
    elif target<l[midpoint]:
        return binary_search(l, target, low,midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
    
if __name__=='__main__':
    l=[1, 4, 6, 9, 12, 14, 18, 25, 29]
    target=18

    print(naive_search(l, target))
    print(binary_search(l, target))

    
