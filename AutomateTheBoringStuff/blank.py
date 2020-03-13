row=['1','2','3','4','5','6','7','8']
column=['a','b','c','d','e','f','g','h']
color=['b','w']
pieces=['king','queen','bishop','knight','rook','pawn']
piecesRange={'wking':[1,1],'wqueen':[0,1],'wbishop':[0,2],
             'wknight':[0,2],'wrook':[0,2],'wpawn':[0,8],
             'bking':[1,1],'bqueen':[0,1],'bbishop':[0,2],
             'bknight':[0,2],'brook':[0,2],'bpawn':[0,8]}


theBoard={'h1':'bking','c6':'wqueen','g2':'bbishop','h5':'bqueen','e3':'wking',
              'a2':'wpawn','b2':'wpawn'}


numberOfPieces={}
for piece in theBoard.values():
    numberOfPieces.setdefault(piece,0)
    numberOfPieces[piece]=numberOfPieces[piece]+1

pieceNumber=0
lowerRange=0
upperRange=0
for x in numberOfPieces:
    pieceNumber=numberOfPieces[x]
    lowerRange=piecesRange[x][0]
    upperRange=piecesRange[x][1]
   
numberOfDiff=0
for y in numberOfPieces.values():
    numberOfDiff=numberOfDiff+int(y)
print(numberOfDiff)


