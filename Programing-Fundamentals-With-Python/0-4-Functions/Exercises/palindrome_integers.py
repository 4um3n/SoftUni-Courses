is_int_palindrome = lambda n: True if n == n[::-1] else False
for n in input().split(", "):
    print(is_int_palindrome(n))