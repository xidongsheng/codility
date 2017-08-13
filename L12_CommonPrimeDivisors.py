
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(A,B):
    # https://codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/
    n = len(A)
    result = 0
    for i in xrange(n):
        a = A[i]
        b = B[i]
        g = gcd(a,b)
        while(g != 1):
            ga=g
            gb=g
            while(a%ga==0 and ga!=1):
                a/=ga
                ga=gcd(a,ga)

            while(b%gb==0 and gb!=1):
                b/=gb
                gb=gcd(b,gb)

            g = gcd(a,b)

        if(a==b):
            result+=1

    return result


if __name__ == "__main__":
    A = [15, 10, 9]
    B = [75, 30, 5]
    print solution(A,B)