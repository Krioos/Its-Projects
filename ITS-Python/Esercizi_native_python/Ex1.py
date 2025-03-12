# Reverse each word of a string
s = input("Insert a string")
reverse_word = ""
reversed_string = ""
for i in range (len(s)):
    if s[i] == " ":
        reverse_word = reverse_word[::-1]
        reversed_string += reverse_word + " "
        reverse_word = ""
    elif i == len(s)-1:
        reverse_word = reverse_word[::-1]
        reversed_string += reverse_word
    else:
        reverse_word += s[i]
print(reversed_string)
