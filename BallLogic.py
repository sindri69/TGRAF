import random

def ballMovement(maze, speed, ori, posX, posZ):
    moves = []
    if ori == "north":
        if not maze.cells[posX][posZ + 1].south: moves.append("north") 
        if not maze.cells[posX][posZ].west: moves.append("west") 
        if not maze.cells[posX + 1][posZ].west: moves.append("east") 
    elif ori == "south":
        if not maze.cells[posX][posZ].south: moves.append("south") 
        if not maze.cells[posX][posZ].west: moves.append("west") 
        if not maze.cells[posX + 1][posZ].west: moves.append("east") 
    elif ori == "east":
        if not maze.cells[posX][posZ + 1].south: moves.append("north") 
        if not maze.cells[posX][posZ].west: moves.append("west") 
        if not maze.cells[posX][posZ].south: moves.append("south") 
    elif ori == "west":
        if not maze.cells[posX][posZ + 1].south: moves.append("north") 
        if not maze.cells[posX][posZ].south: moves.append("south") 
        if not maze.cells[posX + 1][posZ].west: moves.append("east") 
    if not moves:
        if ori == "north": ori = "south"
        if ori == "south": ori = "north"
        if ori == "west": ori = "east"
        if ori == "east": ori = "west"
    ori = random.choice(moves)
    time = speed / 3.0
    return (time, ori)