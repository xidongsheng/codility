
def solution(A, K):
    """
    https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
    :param A:
    :param K:
    :return:
    """

    B = [1] * len(A)

    for inx,value in enumerate(A):
        B[(inx + K) % len(A)] = value

    return B


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    print solution(A,K)