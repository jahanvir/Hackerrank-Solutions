from heapq import heapify, heappush, heappop
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    heapify(A)
    count=0
    while A[0]<k:
        if len(A)<2:
            return -1
        heappush(A, heappop(A)+2*heappop(A))
        count+=1
    return count
        
