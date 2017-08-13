

def solution(A):
    """
    https://codility.com/programmers/lessons/6-sorting/distinct/
    """
    A.sort()

    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])


if __name__ == '__main__':
    A =  [-3, 1, 2, -2, 5, 6]
    print solution(A)