
def solution(A):
    # https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
    # time complexity is O(N*N), don't  fullfill requirements
    temp = []
    for i in range(1,len(A)):
        temp.append( abs(sum(A[0:i]) - sum(A[i:])) )

    return min(temp)


if __name__ == "__main__":
    A = [3,1,2,4,3]
    print solution(A)
