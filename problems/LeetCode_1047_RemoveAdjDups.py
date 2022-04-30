def removeDuplicates(self, s):
    output = []
    for ch in s:
        if output and ch == output[-1]: 
            output.pop()
        else: 
            output.append(ch)
    return ''.join(output)
        
        
print(removeDuplicates("abbacba"))