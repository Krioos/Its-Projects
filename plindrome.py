def palindrome(s:str)-> bool:
        s = s.replace(" ", "").lower()
        if s[0::] == s[::-1]:
            return True
        else:
            return False
        s.replace
        
print(palindrome("madam"))  # True
print(palindrome("hello"))  # False
print(palindrome("i topi non avevano nipoti"))