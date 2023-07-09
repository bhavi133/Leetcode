Link : https://leetcode.com/problems/number-of-senior-citizens/

Code :

def countSeniors(self, details: List[str]) -> int:
    # l = []
    # count = 0
    # for i in details:
    #     l.append(i[-4:-2])
    # for i in l:
    #     if int(i) > 60:
    #         count += 1
    # return count

    # l = [i[-4:-2] for i in details]
    # return len([i for i in l if int(i) > 60])  

    # count = 0
    # for i in details:
    #     if int(i[-4:-2]) > 60:
    #         count += 1
    # return count

    return len([i for i in details if int(i[-4:-2]) > 60])    
