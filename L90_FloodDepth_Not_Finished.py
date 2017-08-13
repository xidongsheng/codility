
def solution(A):
    """
    https://codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/flood_depth/
    """
    n = len(A)
    max_dep = 0
    left_pos = A[0]
    right_pos = A[0]

    for p in xrange(n):
        for q in xrange(p,n):
            if A[q]>=A[p]:
                max_dep = max_dep
            elif A[q]<A[q]:
                max_dep(max_dep, A[q])


if __name__ == '__main__':
    A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
    print solution(A)