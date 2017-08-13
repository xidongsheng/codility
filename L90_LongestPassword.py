import re

def solution(S):
    """
    https://codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/
    """
    _word_re = re.compile(r'^[0-9a-zA-Z]{1,}$')

    words = S.split(' ')
    valid_password_len = []
    for word in words:
        word = word.strip(' ')
        if _word_re.match(word):
            letter_count = len(re.findall('[a-zA-Z]',word))
            digit_count = len(re.findall('[0-9]', word))
            if letter_count%2 == 0 and digit_count%2 ==1:
                valid_password_len.append(len(word))

    if len(valid_password_len) == 0:
        return -1
    else:
        return max(valid_password_len)



if __name__ == '__main__':
    # S = 'test 5 a0A pass007 ?xy1'
    S = 'test'
    print solution(S)