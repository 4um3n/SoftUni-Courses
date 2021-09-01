words = [word for word in input().split() if word == word[::-1]]
palindrome = input()
print(words)
print(f"Found palindrome {words.count(palindrome)} times")
