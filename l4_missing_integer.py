def solution(A):
    # https://codility.com/programmers/lessons/4-counting_elements/missing_integer/
    A.sort()
    for i in range(1, len(A) + 1):
        if i not in A:
            return i

    return A[-1] + 1

if __name__ == "__main__":
    A = [1, 3, 6, 4, 1, 2]
    print solution(A)