# my_diff_tool/my_diff.py

def lcs_lines_function(lines1, lines2):
    m = len(lines1)
    n = len(lines2)
    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]  # Ensure dp entries are lists

    for i in range(m):
        for j in range(n):
            if lines1[i] == lines2[j]:
                dp[i + 1][j + 1] = dp[i][j] + [lines1[i]]
            else:
                if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                    dp[i + 1][j + 1] = dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]

    return dp[m][n]

def generate_diff(lines1, lines2):
    lcs_lines = lcs_lines_function(lines1, lines2)
    diff = []
    i, j = 0, 0
    
    for line in lcs_lines:
        while i < len(lines1) and lines1[i] != line:
            diff.append(f"< {lines1[i]}")
            i += 1
        while j < len(lines2) and lines2[j] != line:
            diff.append(f"> {lines2[j]}")
            j += 1
        diff.append(f"  {line}")
        i += 1
        j += 1
    
    while i < len(lines1):
        diff.append(f"< {lines1[i]}")
        i += 1
    
    while j < len(lines2):
        diff.append(f"> {lines2[j]}")
        j += 1

    return diff

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2-d array to store the length of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array from bottom up
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Following code is used to print lcs
    index = dp[m][n]
    lcs_str = [""] * (index + 1)
    lcs_str[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_str)
