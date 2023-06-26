Link : https://leetcode.com/problems/count-items-matching-a-rule/

Code :

def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    l = []
    for i in items:
        if ruleKey == "type" and i[0] == ruleValue:
            l.append(i)
        elif ruleKey == "color" and i[1] == ruleValue:
            l.append(i)
        elif ruleKey == "name" and i[2] == ruleValue:
            l.append(i)
    return len(l)
