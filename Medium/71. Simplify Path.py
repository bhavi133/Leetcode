Link : https://leetcode.com/problems/simplify-path/

Code :

def simplifyPath(self, path: str) -> str:
    path = path.split('/')
    l = []
    for i in path:
        if i == "..":
            if l:
                l.pop()
        elif i != "." and i != "":
            l.append(i)
    return '/' + '/'.join(l)
