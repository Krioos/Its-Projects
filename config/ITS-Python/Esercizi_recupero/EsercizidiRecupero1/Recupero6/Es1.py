def recursivePalindrome(stringa:str)-> bool:
    stringa = stringa.lower().replace(" ", "")
    if len(stringa) == 1 or len(stringa) == 0:
        return True
    elif stringa[0] == stringa[-1]:
        return recursivePalindrome(stringa[1:-1])
    else:
        return False
    
print(recursivePalindrome("Radar"))
print(recursivePalindrome("I topi non avevano nipoti"))
print(recursivePalindrome("casa"))