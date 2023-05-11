# Initialize game board
game_board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
              ['#', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
              ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
              ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#'],
              ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
              ['#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
              ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

# Initialize Pacman's starting position
pacman_position = [1, 1]

# Function to move Pacman up
def move_up():
    global pacman_position
    x, y = pacman_position
    if game_board[x-1][y] != '#':
        pacman_position = [x-1, y]

# Function to move Pacman down
def move_down():
    global pacman_position
    x, y = pacman_position
    if game_board[x+1][y] != '#':
        pacman_position = [x+1, y]

# Function to move Pacman left
def move_left():
    global pacman_position
    x, y = pacman_position
    if game_board[x][y-1] != '#':
        pacman_position = [x, y-1]

# Function to move Pacman right
def move_right():
    global pacman_position
    x, y = pacman_position
    if game_board[x][y+1] != '#':
        pacman_position = [x, y+1]
