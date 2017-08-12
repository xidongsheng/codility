
def solution(X,Y,D):
    # https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/
    step = (Y - X)/D
    remainder = (Y - X)%D
    if remainder == 0:
        return step
    else:
        return step + 1

if __name__ == "__main__":
    X = 10
    Y = 85
    D = 30
    print solution(X,Y,D)
