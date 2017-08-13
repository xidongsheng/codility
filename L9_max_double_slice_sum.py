
def solution(A):
    """
    https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
    time complexity O(n*3)
    """
    n = len(A)
    max_double_slice = 0
    for p in xrange(n):
        for q in xrange(p+1,n):
            for m in xrange(q+1,n):
                sum_double_slice = sum(A[p+1:q]) + sum(A[q+1:m])
                max_double_slice = max(max_double_slice,sum_double_slice)

    return max_double_slice


def solution_bad(A):
    """
    time complexity O(n*3)
    """
    n = len(A)
    max_double_slice = 0
    for p in xrange(n):
        for q in xrange(p+1,n):
            for m in xrange(q+1,n):
                sum_double_slice = sum(A[p+1:q]) + sum(A[q+1:m])
                max_double_slice = max(max_double_slice,sum_double_slice)

    return max_double_slice



if __name__ == '__main__':
    A =  [3, 2, 6, -1, 4, 5, -1, 2]

    print solution(A)