def longestPalindrome(string):
    n = len(string)

    if (n<2):
        return n

    start = 0
    maxlength = 1

    for i in range(n):
        low = i - 1
        high = i + 1

        while (high < n and string[high] == string[i]):
            high = high + 1

        while (low >= 0  and string[low] == string[i]):
            low = low-1

        while (low >= 0 and high < n and string[low] == string[high]):
            low = low-1
            high = high+1

        length = high - low - 1
        if (maxlength < length):
            maxlength = length
            start = low + 1

    print("Longest Palindrome Substring is : ", end=" ")
    print(string[start:start + maxlength])

    return maxlength

string = ("babad")
print("Lenght is : " + str(longestPalindrome(string)))