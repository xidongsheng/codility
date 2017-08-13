
def solution(K, A):
    """
    https://codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes
    """
    n = len(A)
    sum_ropes = 0
    max_num = 0
    for i in xrange(n):
        sum_ropes += A[i]
        if sum_ropes >= K:
            max_num += 1
            sum_ropes = 0

    return max_num



if __name__ == '__main__':
    A = [1, 2, 3, 4, 1, 1, 3]
    K = 4
    print solution(K, A)