a=str(input("Enter the word:"))
a=a.casefold()
print(a)
reverse_word=a[::-1]
print(reverse_word)
if a==reverse_word:
    print("It's a panildrome word!")
else:
    print("It's not a palindrome word!")