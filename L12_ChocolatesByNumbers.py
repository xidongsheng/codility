
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def solution(N,M):
    # https://codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

    multiple = N * M / gcd(N,M)
    return multiple/M




def solution_bad(N,M):
    # https://codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

    eated = [0]
    eated_last = 0
    eated_cur = -1

    while eated_cur not in eated[:-2]:
        eated_cur = (eated_last + M) % N
        eated.append(eated_cur)
        eated_last = eated_cur

    return len(eated) - 1



if __name__ == "__main__":
    N = 10
    M = 4
    print solution(N,M)
