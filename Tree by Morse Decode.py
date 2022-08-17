class Node:
    def __init__(self, key:str):
        self.left = None
        self.right = None
        self.key = key
class BinaryTree:
    # level 0
    root  = Node('None')
    # level 1
    root.left = Node('E')
    root.right = Node('T')
    # level 2
    rll = root.left
    rlr = root.right
    rll.left = Node('I')
    rll.right = Node('A')
    rlr.left = Node('N')
    rlr.right = Node('M')
    # level 3
    rlll = rll.left
    rllr = rll.right
    rlrl = rlr.left
    rlrr = rlr.right
    rlll.left = Node('S')
    rlll.right = Node('U')
    rllr.left = Node('R')
    rllr.right = Node('W')
    rlrl.left = Node('D')
    rlrl.right = Node('K')
    rlrr.left = Node('G')
    rlrr.right = Node('O')
    # level 4
    rllll = rlll.left
    rlllr = rlll.right
    rllrl = rllr.left
    rllrr = rllr.right
    rlrll = rlrl.left
    rlrlr = rlrl.right
    rlrrl = rlrr.left
    rlrrr = rlrr.right
    rllll.left = Node('H')
    rllll.right = Node('V')
    rlllr.left = Node('F')
    rllrl.left = Node('L')
    rllrr.left = Node('P')
    rllrr.right = Node('J')
    rlrll.left = Node('B')
    rlrll.right = Node('X')
    rlrlr.left = Node('C')
    rlrlr.right = Node('Y')
    rlrrl.left = Node('Z')
    rlrrl.right = Node('Q')

def Decoding(str):
    compare = list(str)
    curNode = BinaryTree.root

    for i in range(len(str)):
        if compare[i] == '.':
            curNode = curNode.left
        elif compare[i] == '-' :
            curNode = curNode.right

    return curNode.key
    
### 모르스 부호 Table
table = [('A','.-'),('B','-...'),('C','-.-.'),('D','-..'),
        ('E','.'),('F','..-.'),('G','--.'),('H','....'),
        ('I','..'),('J','.---'),('K','-.-'),('L','.-..'),
        ('M','--'),('N','-.'),('O','---'),('P','.--.'),
        ('Q','--.-'),('R','.-.'),('S','...'),('T','-'),
        ('U','..-'),('V','...-'),('W','.--'),('X','-..-'),
        ('Y','-.--'),('Z','--..') ]

### Morse Code 변환 Table
morse = []

# 영문 대문자 입력 외 예외처리
try: 
    x = input("입력 문장 : ")
    if x.isupper() == False:
        raise
except:
    print("영문 대문자 A~Z만 입력해 주세요.")

# 영문 대문자 입력시 실행 
else:
    morse = list(x)

    # Encoding
    for i in range(len(x)):
        # Encoding O(1)
        morse[i] = table[ord(morse[i])-ord('A')][1]
        
    # Morse Code
    print("Morse Code : ", morse)

    # Decoding
    for i in range(len(morse)):
        # Decoding O(logN)
        morse[i] = Decoding(morse[i])
    print("Decoding : ", "".join(morse))