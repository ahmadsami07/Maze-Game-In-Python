# My Mario Game
# Description:A Mario game, where there is a maze a user has to navigate through, which has bombs and treasures which decrease and increases the player's score respectively.
# Author: Ahmad As Sami(301404717)
# Date:28 July 2019

# -------------------------------------------------------------------
  
def readDataFileAndSetVariables( filename ):
    # Make the following variables accessible in this function by making them "global"
    global mazeWidth
    global mazeHeight
    global aNumOfTreasures
    global aNumOfBombs
    global emptyCell
    global treasure
    global bomb
    global mario
    global exitGate
    global boundary
    global boundarySide
    global marioLocationList
    global rList
    global eList
    global bombScoreRatio

    # Open file for reading
    dataFileRead = open(filename, "r")
    # Read file content into a list - to be completed - Part 1
    mygamelist=list(dataFileRead)
    
    #The \n is stripped out from the new list.
    for i in range(len(mygamelist)):
      if "\n" in mygamelist[i]:
        mygamelist[i]=mygamelist[i].strip("\n")
    

    #All the variables are given the corresponding data according to their corresponding indexes in the new list from the data file.
    mazeWidth=int(mygamelist[0])
    mazeHeight=int(mygamelist[1])
    aNumOfTreasures=int(mygamelist[2])
    aNumOfBombs=int(mygamelist[3])
    emptyCell=mygamelist[4]
    treasure=mygamelist[5]
    bomb=mygamelist[6]
    mario=mygamelist[7]
    exitGate=mygamelist[8]
    boundary=mygamelist[9]
    boundarySide=mygamelist[10]
    marioLocationList=[list(mygamelist[11].split(" "))]

    #For the lists of coordinates for the bombs and treasure, they are appended in according to the length of each corresponding amount of data in the file.

    for i in range(15):
      rList.append(list((mygamelist[12+i]).split(" ")))
    for i in range(30):
      eList.append(list((mygamelist[27+i]).split(" ")))
    bombScoreRatio=int(mygamelist[57])


# For debugging purposes
    #print("mazeWidth = ", mazeWidth)
    #print("mazeHeight = ", mazeHeight)
    #print("aNumOfTreasures = ", aNumOfTreasures)
    #print("aNumOfBombs = ", aNumOfBombs)
    #print("emptyCell = '{}'".format(emptyCell))
    #print("treasure = '{}'".format(treasure))
    #print("bomb = '{}'".format(bomb))  
    #print("mario = '{}'".format(mario))    
    #print("exitGate = '{}'".format(exitGate))
    #print("boundary = '{}'".format(boundary))    
    #print("boundarySide = '{}'".format(boundarySide))
    #print("marioLocationList = ", marioLocationList)
    #print("rList = ", rList)
    #print("eList = ", eList)
    #print("bombScoreRatio = ", bombScoreRatio)

    # Close the file
    dataFileRead.close( )
    return

# -------------------------------------------------------------------

def createMaze(aMaze, aWidth, aHeight, aCell):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "cell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]   
    #printMaze(aMaze,aHeight)  
   #for debugging purposes - Print maze as a list of list
    return aMaze

# -------------------------------------------------------------------

# Print Maze - for debugging purposes
def printMaze(aMaze, aHeight):
    ''' Print "aMaze" of "aHeight" - for debug purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundary(aWidth, bH):
    ''' Create and return a list that contains 2 lists: the top boundary of the maze
        and the bottom boundary of the maze. Each element of these 2 lists is a string set to "bH".
    '''
    return list([[(bH) for number in range(aWidth)],[(bH) for number in range(aWidth)]])                

# -------------------------------------------------------------------

def displayMaze(aMaze, aWidth, aHeight, hBoundary, bS ):
    ''' Display 'aMaze' with column numbers at the top and row numbers to the left of each row
        along with the top and the bottom boundaries "hBoundary" that surround the maze.

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "bS" is the symbol used for the vertical border.

        No returned value
    '''
    topIndex = 0  # Index of proper boundary in hBoundary
    bottomIndex = 1
    offset = 3
    aString = (offset+1) * " "

    print()  
    # Display a row of numbers from 1 to aWidth
    for column in range(aWidth):
        aString = aString + str(column+1) + " "
        if len(str(column+1)) == 1 :
            aString += " "           
    print(aString)

    # Display the top boundary of maze
    print(offset * " " + "".join(hBoundary[topIndex]))
    
    # Display a column of numbers from 1 to aHeight + left and right boundaries of the maze
    for row in range(aHeight):
        pre = str(row+1) + " " + bS
        if row >= 9: # i.e., displayed row number is >= 10 - adjusting for extra digit
           pre = str(row+1) + bS
        post = bS
        aRow = pre + ''.join(aMaze[row]) + post
        print(aRow)

    # Display the bottom boundary of maze
    print(offset * " " + "".join(hBoundary[bottomIndex]))
    return

# -------------------------------------------------------------------

def placeInMaze(aMaze, aRow, aColumn, aContent):
    ''' Place something represented by "aContent" at the location ["aRow", "aColumn"] into "aMaze"

        Returned value:
         "aMaze" updated.
    '''
    aMaze[aRow][aColumn] = aContent
    return aMaze

# -------------------------------------------------------------------

def placeExitGate(aWidth, aHeight, rowMario, columnMario, hBoundary, exitGate):
    ''' Place the exit gate, represented by "exitGate", at the opposite corner of Mario's location.
		This means:
		Place the exit gate either in the top boundary or the bottom boundary 
		which ever is at the opposite corner of Mario's location, represented by [rowMario, columnMario].

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.

        Returned value:
         "hBoundary" updated.
         "hBoundary" is a list of 2 lists: the first list is the top boundary and the second list is the bottom boundary.
         "exitGateLocationList" updated.
    '''
    topIndex = 0 # Index of proper boundary in hBoundary
    bottomIndex = 1
    exitGateRight = False
    exitGateBottom = False
    row = 0
    column = 1
    exitGateLocationList.insert(row, 0)   # Assume exit gate at the top left
    exitGateLocationList.insert(column, 0)
        
    # Where is Mario?
    # If Mario is top left then exit gate is bottom right
    if columnMario <= ((aWidth) // 2) : # Mario on the left?
        exitGateLocationList[column] = aWidth - 1  # Yes, then exit gate on the right
        exitGateRight = True
    # No, then assuption holds -> exit gate on the left
    if rowMario <= ((aHeight) // 2) :   # Mario at the top?
        exitGateLocationList[row] = aHeight - 1    # Yes, then exit gate at the bottom
        exitGateBottom = True
        # No, then assuption holds -> exit gate at the top

    # Place exit gate in appropriate top/bottom boundary
    if exitGateBottom :
        del hBoundary[bottomIndex][exitGateLocationList[column]]
        hBoundary[bottomIndex].insert(exitGateLocationList[column], exitGate)
    else:
        del hBoundary[topIndex][exitGateLocationList[column]]
        hBoundary[topIndex].insert(exitGateLocationList[column], exitGate)       

    
    return hBoundary, exitGateLocationList  # Can return a tuple -> elements sepatared by a coma

# -------------------------------------------------------------------

def setMarioScore(numOfBombs, divideBy):
    ''' Set and return Mario's score to be numOfBombs // divideBy
    '''    
    return numOfBombs // divideBy

# -------------------------------------------------------------------


# Main part of the program

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
filename = input("Please, enter a filename: ")

# Initialize the game variables ...
mazeWidth = 0
mazeHeight = 0
aNumOfTreasures = 0
aNumOfBombs = 0
emptyCell = ""
treasure = "" 
bomb = ""
mario = ""  
exitGate = ""  
boundary = ""  
boundarySide = ""
marioLocationList = list()
rList = list()
eList = list()
bombScoreRatio = 0

# ... and assign them values coming form the input data file (filename)
readDataFileAndSetVariables(filename)

# Create a maze
theMaze = list()
theMaze = createMaze(theMaze, mazeWidth, mazeHeight, emptyCell)

# Create the boundary around the maze (not part of the maze)
hBoundary = list()
hBoundary = createBoundary(mazeWidth, boundary)

# Place treasures in the maze
rowIndex = 0
columnIndex = 1  
for obstacle in range(aNumOfTreasures):
    theMaze = placeInMaze(theMaze, int(rList[obstacle][rowIndex]), int(rList[obstacle][columnIndex]), treasure)

# Place bombs in the maze
for obstacle in range(aNumOfBombs):
    theMaze = placeInMaze(theMaze, int(eList[obstacle][rowIndex]), int(eList[obstacle][columnIndex]), bomb)

# Place Mario in the maze
theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), mario)
          
# Create exit gate and place it in the maze
# Place the exit gate at the opposite corner of Mario's location
exitGateLocationList = list()
hBoundary, exitGateLocationList = placeExitGate(mazeWidth, mazeHeight, int(marioLocationList[0][0]), int(marioLocationList[0][1]), hBoundary, exitGate)

# Set Mario's score

# Part 2 - To be completed
# Here is the 'high-level' algorithm:

# As long as the player is playing ...

	
	# Once you have completed Part 1, uncomment the following Python statement and see what is displayed on the screen!

playgame=True

marioScore = setMarioScore(aNumOfBombs, bombScoreRatio)
	# Display Mario's score (see Sample Runs)
while playgame:
# Display the maze
  displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)

  # Display Mario's score (see Sample Runs)
  print("Mario's score -> {}".format(marioScore))

  #If Mario's score falls to zero, the loop will break and the program will terminate.
  if marioScore==0:
    print("Mario's Score is now down to 0! You have lost!")
    playgame=False
    break


	# Display instructions to the player (see Sample Runs)
  playerchoice=input("Move Mario by entering the letter 'r' for right, 'l' for left, 'u' for up and 'd' for down, 'x' to exit the game:").lower()
    
  #If the player chooses x, the game will terminate.
  
  if playerchoice=="x":
    playgame=False
    break



  #Presing r will make Mario move right.
  elif playerchoice=='r':
    #The following will adjust Mario's location to a new position in the maze.
    marioLocationList[0][1]=int(marioLocationList[0][1])+1
   
    #This stores the initial location of Mario.
    initiallocation=[[(marioLocationList[0][0]),int(marioLocationList[0][1]-1)]]
    

   #If there is a bomb in the new location, the player's score will be reduced by one. If there is treasure, score
    treasureo=True
    
    for i in range(len(eList)):
      if eList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
        marioScore-=1
        treasureo=False
    
    if treasureo:
        for i in range(len(rList)):
          if rList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
              marioScore+=1
          

    #Using the PlaceInMaze function the Mario is placed into that particular index of the maze.
    placeInMaze(theMaze,int(marioLocationList[0][0]),int(marioLocationList[0][1]),mario)

    #The following changes the maze back to how it was after Mario has crossed this location, by going back to initial location.
    placeInMaze(theMaze,int(initiallocation[0][0]),int(initiallocation[0][1]),treasure)
  


  #Pressing l will make mario move left.
  elif playerchoice=='l':
    #The following will adjust Mario's location to a new position in the maze.
    marioLocationList[0][1]=int(marioLocationList[0][1])-1

    #This stores the initial location of Mario.
    initiallocation=[[(marioLocationList[0][0]),int(marioLocationList[0][1]+1)]]

     #If there is a bomb in the new location, the player's score will be reduced by one.
    treasureo=True
    
    for i in range(len(eList)):
      if eList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
        marioScore-=1
        treasureo=False
    
    if treasureo:
        for i in range(len(rList)):
          if rList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
              marioScore+=1
      
    #Using the PlaceInMaze function the Mario is placed into that particular index of the maze.
    placeInMaze(theMaze,int(marioLocationList[0][0]),int(marioLocationList[0][1]),mario)

    

    #The following changes the maze back to how it was after Mario has crossed this location, by going back to initial location.
    placeInMaze(theMaze,int(initiallocation[0][0]),int(initiallocation[0][1]),emptyCell)



  #If Mario reaches the exit gate, the player wins the game, and the maze is displayed for thelast time. This is only for up and down commands, as the exit cannot be accessed from the right or down inputs.
  if marioLocationList==[[0,0]]:
      displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)
      print("Mario has reached the exit gate with a score of {}! You win!".format(marioScore))
      playgame=False
      break




  #Pressing u will make mario move up.
  elif playerchoice=='u':

    #The following will adjust Mario's location to a new position in the maze.
    marioLocationList[0][0]=int(marioLocationList[0][0])-1

    #This stores the initial location of Mario.
    initiallocation=[[int(marioLocationList[0][0]+1),int(marioLocationList[0][1])]]


    #If there is a bomb in the new location, the player's score will be reduced by one.
    treasureo=True
    
    for i in range(len(eList)):
      if eList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
        marioScore-=1
        treasureo=False
    
    if treasureo:
        for i in range(len(rList)):
          if rList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
              marioScore+=1

    #Using the PlaceInMaze function the Mario is placed into that particular index of the maze.
    placeInMaze(theMaze,int(marioLocationList[0][0]),int(marioLocationList[0][1]),mario)

    #The following changes the maze back to how it was after Mario has crossed this location, by going back to initial location.
    placeInMaze(theMaze,int(initiallocation[0][0]),int(initiallocation[0][1]),emptyCell)

    #If Mario reaches the exit gate, the player wins the game, and the maze is displayed for thelast time. This is only for up and down commands, as the exit cannot be accessed from the right or down inputs.

  if marioLocationList==[[0,0]]:
      displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)
      print("Mario has reached the exit gate with a score of {}! You win!".format(marioScore))
      playgame=False
      break

  #Pressing d will make mario move down.
  elif playerchoice=='d':


    #The following will adjust Mario's location to a new position in the maze.
    marioLocationList[0][0]=int(marioLocationList[0][0])+1

    #This stores the initial location of Mario.
    initiallocation=[[int(marioLocationList[0][0]-1),int(marioLocationList[0][1])]]

    #If there is a bomb in the new location, the player's score will be reduced by one.
    
    
    treasureo=True
   
    for i in range(len(eList)):
      if eList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
        marioScore-=1
        treasureo=False
    
    if treasureo:
        for i in range(len(rList)):
          if rList[i]==list([str(marioLocationList[0][0]),str(marioLocationList[0][1])]):
              marioScore+=1
    #Using the PlaceInMaze function the Mario is placed into that particular index of the maze.
    placeInMaze(theMaze,int(marioLocationList[0][0]),int(marioLocationList[0][1]),mario)

    #The following changes the maze back to how it was after Mario has crossed this location, by going back to initial location
    placeInMaze(theMaze,int(initiallocation[0][0]),int(initiallocation[0][1]),emptyCell)
  
 
  

	

print("\n-------")
