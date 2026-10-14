class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { "}" : "{", "]" : "[", ")" : "("}
        container = []
        for char in s:
            #If the char is in open item mapping then add to container stack
            #Else if its not an open item check top of stack if we have match pop from contaainer stack
                #If its not in container stack when checked return false
            if char not in mapping:
                container.append(char)
            elif container and mapping[char] == container[-1]:
                container.pop()
            else:
                return False
        return not container