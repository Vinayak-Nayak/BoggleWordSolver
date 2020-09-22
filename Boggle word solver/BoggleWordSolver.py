#enter 16 alphates
#input example
'''
     a
     b
     c
     d
     .
     .
     .
     p
'''
class Tree():
    def __init__(self, letter = None):
        self.letter = letter
        self.children = {}
        self.leaf = False

    #add a word letter by letter
    def add(self, word):
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = Tree(letter)
            return self.children[letter].add(word)
        else:
            self.leaf = True
            return self

    #locate a letter in the tree
    def search(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]

#function for actual word solver
def findword(board, tree, validated, row, col, path = None, currletter = None, word = None):
    letter = board[row][col]
    if path is None or currletter is None or word is None:
        currletter = tree.search(letter)
        path = [(row, col)]
        word = letter
    else:
        currletter = currletter.search(letter)
        path.append((row, col))
        word = word + letter
    
    #Base Cases
    if currletter is None:  #denotes prefix does not exist in dictionary
        return
    if currletter.leaf:  #denotes a valid word
        validated.add(word)
    
    # recursive call
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if(r>=0 and r<4 and c>=0 and c<4 and r!=row and c!=col and (r,c) not in path):
                findword(board, tree, validated, r, c, path[:], currletter, word[:])
    

def main():
    #initialize a game board based on user input
    board = []
    for i in range(0,4):
        #append empty row
        board.append([])
        for j in range(0,4):
            board[i].append(input().strip().upper())

    #print board
    for i in range(0,4):
        for j in range(0,4):
            print(board[i][j], end = " ")
        print()

    #load dictionary
    dict = open('dictionary-yawl.txt', "r")

    tree = Tree()
    for line in dict:
        word = line.rstrip().upper()
        tree.add(word)

    #set to store strings that match valid words found in dictionary
    validated = set()

    for row in range(0,4):
        for col in range(0,4):
            findword(board, tree, validated, row, col)

    for word in sorted(validated):
        if len(word) > 2:
            print(word)

main()
