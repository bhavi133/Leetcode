Link : https://leetcode.com/problems/min-stack/

Code :

def __init__(self):
    self.stack = []

def push(self, val):
    self.stack.insert(0, val)

def pop(self):
    if len(self.stack) == 0:
        return -1
    else:
        return self.stack.pop(0)
    
def top(self):
    if len(self.stack) == 0:
        return -1
    else:
        return self.stack[0]
    
def getMin(self):
    if len(self.stack) == 0:
        return -1
    else:
        return min(self.stack)
