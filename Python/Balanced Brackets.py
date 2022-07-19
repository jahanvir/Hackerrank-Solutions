def isValid(left,right):
    if (left=='[' and right==']') or (left=='(' and right==')') or (left=='{' and right=='}'):
        return True
    
        return False
    

def isBalanced(s):
    arr=[]
    for b in s:
        if b=='[' or b=='{' or b=='(':
            arr.append(b)
        else:
            if len(arr)==0:
                return "NO"
            last=arr.pop()
            if not isValid(last,b):
                return "NO"
    if len(arr)!=0:
        return "NO"
    return "YES"
