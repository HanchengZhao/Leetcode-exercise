# longest common substring
# https://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php

# dp solution
# use a table to store the length of current longest common string,
# replace the string if the length is longer


def lcs(s, p):
    m, n = len(s), len(p)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    string = ""
    for i in range(m):
        for j in range(n):
            if s[i] == p[j]:
                l = dp[i][j] + 1
                dp[i+1][j+1] = l
                if l > len(string):
                    string = s[i-l+1: i+1]
                    print(string)
    return string


print(lcs('academy',  'abracadabra'))
# acad
