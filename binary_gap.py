# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    """
    lessons test by codility
    https://codility.com/programmers/lessons/1-iterations/binary_gap/
    :param N:integer
    :return: binary gap
    """
    # change integer to string
    bin_str = bin(N).replace('0b', '')

    # find all 1 postions
    one_pos = []
    for idx,v in enumerate(bin_str):
        if v == '1':
            one_pos.append(idx)

    # calculate max binary gap
    binary_gap = 0
    for i in range(len(one_pos) - 1 ):
        gap = one_pos[i+1] - one_pos[i] - 1
        if gap > binary_gap:
            binary_gap = gap

    return binary_gap


def solution2(N):
    'https://codesays.com/2014/solution-to-binary-gap-by-codility/'
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        N //= 2

    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2

    return max_gap


if __name__ == '__main__':
    A = 529
    print solution(A)