Link : https://leetcode.com/problems/determine-color-of-a-chessboard-square/

Code :

def squareIsWhite(self, coordinates: str) -> bool:
    # black = ['a1','a3','a5','a7','b2','b4','b6','b8','c1','c3','c5','c7','d2','d4','d6','d8','e1','e3','e5','e7','f2','f4','f6','f8','g1','g3','g5','g7','h2','h4','h6','h8']
    # return coordinates not in black

    return (ord(coordinates[0]) - 96 + int(coordinates[1])) % 2
