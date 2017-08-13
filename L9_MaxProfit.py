
def solution(A):
    """
    https://codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
    """
    max_profit =  0
    if len(A) != 0:
        min_a = A[0]
        for a in A:
            max_profit = max(max_profit, a - min_a)
            min_a = min(a,min_a)

    return max_profit


def solution_bad(A):
    """
    time complexity O(n*2)
    """
    n = len(A)
    max_profit = 0
    for p in xrange(n):
        for q in xrange(p):
            max_profit = max(max_profit, A[p] - A[q])

    return max_profit



if __name__ == '__main__':
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    print solution(A)