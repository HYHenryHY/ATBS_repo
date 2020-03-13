#Chess Dictionary Validator
# Objective: function that takes our dictionary argument and returns True
# or False depending on if board is valid

theBoard={'h1':'bking','c6':'wqueen','g2':'bbishop','h5':'bqueen','e3':'wking',
              'a2':'wpawn','b2':'wpawn'}

def isValidChessBoard(board):   
    row=['1','2','3','4','5','6','7','8']
    column=['a','b','c','d','e','f','g','h']
    piecesRange={'wking':[1,1],'wqueen':[0,1],'wbishop':[0,2],
             'wknight':[0,2],'wrook':[0,2],'wpawn':[0,8],
             'bking':[1,1],'bqueen':[0,1],'bbishop':[0,2],
             'bknight':[0,2],'brook':[0,2],'bpawn':[0,8]}
    
    #check if key is on the chess board
    boardKeyList=list(theBoard.keys()) #output: ['h1', 'c6', 'g2', 'h5', 'e3', 'a2', 'b2']
    for k in boardKeyList: #creates single list for each Key ['h1']
        singleKey=[]
        singleKey.append(k) 
        for s in singleKey: #creates new lists with each character in list ['h', '1']
            splitSingleKey=[]
            splitSingleKey=list(s)
            for c in splitSingleKey: #puts individual character in their own list ['h']
                keyCharacter=[]
                keyCharacter=list(c)
                if keyCharacter[0] not in row and keyCharacter[0] not in column:
                    return False

    
    #counting the number of different pieces
    numberOfPieces={}
    for piece in board.values():
        numberOfPieces.setdefault(piece,0)
        numberOfPieces[piece]=numberOfPieces[piece]+1

    #check if number of pieces is in the valid range for that specific piece
    pieceNumber=0 #a variable that stores number of pieces for each loop
    lowerRange=0 #variable that stores lower Range for pur piece
    upperRange=0
    for x in numberOfPieces:
        pieceNumber=numberOfPieces[x] #assigns the values from the keys in numberOfPieces
        lowerRange=piecesRange[x][0] #assigns the range from piecesRange
        upperRange=piecesRange[x][1] #
        if not lowerRange <= pieceNumber <= upperRange: #checks if the number of pieces in our range
            return False
    
    
    
    return True #end of our function

isValidChessBoard(theBoard) #calls our function
print(isValidChessBoard(theBoard)) #prints the output (True/False) from our function
    
