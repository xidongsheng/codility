

def solution(A):
    """
    https://codility.com/programmers/lessons/6-sorting/distinct/
    :param A:
    :return:
    """

    n = len(A)
    if n == 0:
        distinct = 0
    else:
        distinct = 1
        A.sort()

        for i in xrange(1,n):
            if A[i] == A[i-1]:
                continue
            else:
                distinct += 1

    return distinct

def solution_bad(A):

    n = len(A)
    if n != 0:
        uniq = [A[0]]
        for i in xrange(1,n):
            if A[i] not in uniq:
                uniq.append(A[i])
        return len(uniq)

    else:
        return 0



if __name__ == '__main__':
    A =  [2, 1, 1, 2, 3, 1]
    print solution(A)