import time
from random import randint

class Cell:
    def __init__(self):
        """
        Initializes status of cell (dead by default)
        """
        self._alive = False

    def setDead(self):
        """
        Modifies living status of cell to dead
        """
        self._alive = False

    def setAlive(self):
        """
        Modifies living status of cell to alive
        """
        self._alive = True

    def isAlive(self):
        """
        Returns living status of cell
        """
        return self._alive

    def printCharacter(self):
        """
        Returns character to print: * for alive; whitespace for dead
        """
        if self._alive:
            return '*'

        return ' '


class GameOfLife:
    def __init__(self, rows = 20, columns = 20, seed = 10):
        """
        Initializes attributes of class GOL
        """
        self.rows = rows
        self.columns = columns
        self.seed = seed

        #create a 2D list of cells
        self.board = [[Cell() for column_cells in range(self.columns)] for row_cells in range(self.rows)]

        #generate initial board
        for row in self.board:
            for column in row:
                #Let the probability of live cells be a third
                state = randint(3, self.seed)
                if state == 3:
                    column.setAlive()
        
        #apply our rules to our first generation
        self.nextPattern()

    def neighbourSum(self, row, column):
        """
        Computes and returns number of live neighbours of cell board[i][j]
        """

        #find all valid neighbours for current cell
        all_neighbours = self.findNeighbours(row, column)

        #generate a list of all live neighbour cells for current cell
        alive_neighbours = []

        for neighbour in all_neighbours:
            if neighbour.isAlive():
                alive_neighbours.append(neighbour)

        return len(alive_neighbours)


    def nextPattern(self):
        """
        changes boards current pattern to the next one according to the game's rules
        """
        gets_to_live = []
        gets_to_die = []

        for row in range(len(self.board)):
            for column in range(len(self.board)):
                
                current_cell = self.board[row][column]

                #extract a list of all neighbouring cells that are alive
                alive_neighbours = self.neighbourSum(row, column)

                if current_cell.isAlive():

                    #underpopulations or overcrowding
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        gets_to_die.append(current_cell)

                    #optimum living conditions
                    if alive_neighbours == 3 or alive_neighbours == 2:
                        gets_to_live.append(current_cell)

                else:
                    #reproduction
                    if alive_neighbours == 3:
                        gets_to_live.append(current_cell)

        #update living status for cells
        for cell in gets_to_live:
            cell.setAlive()

        for cell in gets_to_die:
            cell.setDead()

    def findNeighbours(self, row, column):
        """
        Checks all neighbours of a cell and returns a list of valid neighbour cells
        """

        neighbours = []
        neighbours.append(self.board[(row - 1 + self.rows) % self.rows][(column - 1 + self.columns) % self.columns])
        neighbours.append(self.board[(row - 1 + self.rows) % self.rows][column])
        neighbours.append(self.board[(row - 1 + self.rows) % self.rows][(column + 1) % self.columns])
        neighbours.append(self.board[row % self.rows][(column + 1) % self.columns])
        neighbours.append(self.board[(row + 1) % self.rows][(column + 1) % self.columns])
        neighbours.append(self.board[(row + 1) % self.rows][column])
        neighbours.append(self.board[(row + 1) % self.rows][(column - 1 + self.columns) % self.columns])
        neighbours.append(self.board[row][(column - 1 + self.columns) % self.columns])

        return neighbours


    def printBoard(self):
        """
        prints current pattern replacing 0's with whitespaces and 1's with *s
        """
        for row in self.board:
            for column in row:
                print(column.printCharacter(), end='')
            print()


def main_menu():
    """
    Allows user to select initial pattern
    """

    data = """

    ****** Initial patterns ******
    Pattern 4
    Pattern 5
    Pattern 6

    Note: Any wrong selection will lead to a default pattern

    """
    print(data)
    for i in range(4, 7):
        time.sleep(1.5)
        print("-------------------------------------------\n")
        print("             <<<Pattern {}>>>              \n".format(i))

        pattern = GameOfLife(20, 20, i)
        pattern.printBoard()

        print("-------------------------------------------\n")


    default = 6
    try:
        choice = int(input("Select an initial pattern (integers only): "))

        if choice in [4, 5, 6]:
            return choice

        return default
    except:
        return default


def main():
    """
    Launches the game of life
    """

    seed = main_menu()

    game_of_life = GameOfLife(170, 170, seed)
    game_of_life.printBoard()

    done = False #we are not done playing the game
    while not done:
            game_of_life.nextPattern()
            game_of_life.printBoard()


if __name__ == '__main__':
    main()

