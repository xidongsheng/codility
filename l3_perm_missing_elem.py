
def solution(A):
    # https://codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
    n = len(A) + 1
    sumOfAll = n*(n+1)/2
    curSum = 0
    for i in range(0,len(A)):
        curSum += A[i]

    return sumOfAll-curSum


if __name__ == "__main__":
    A = [2,3,1,5]
    print solution(A)
