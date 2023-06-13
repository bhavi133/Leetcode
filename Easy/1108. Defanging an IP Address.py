Link : https://leetcode.com/problems/defanging-an-ip-address/

Code :

def defangIPaddr(self, address: str) -> str:
    # return "[.]".join(address.split('.'))

    return address.replace('.', '[.]')
