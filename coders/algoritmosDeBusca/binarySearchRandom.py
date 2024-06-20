import random
import time

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
    length=10000

    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list=sorted(list(sorted_list))

    start=time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end=time.time()
    print('Binary search time: ', (end-start)/length,' seconds')
