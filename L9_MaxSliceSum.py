
def solution(A):
    """
    https://codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
    """
    n = len(A)
    max_slice =  A[0]
    max_ending = A[0]
    for i in xrange(1,n):
        max_ending = max(A[i], max_ending + A[i])
        if max_ending > max_slice:
            max_slice = max_ending

    return max_slice



def solution_bad(A):
    """
    O(n*2)
    """
    n = len(A)
    max_slice =  A[0]
    for p in xrange(n):
        for q in xrange(p,n):
            max_slice = max(max_slice,sum(A[p:q]))

    return max_slice





if __name__ == '__main__':
    A = [3, 2, -6, 4, 0]
    print solution(A)