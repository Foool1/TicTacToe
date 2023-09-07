Simple TicTacToe Game in Python
This is a basic implementation of the classic TicTacToe game in Python, playable in the console. The game allows you to play against a simple AI opponent that makes random moves.

How to Play
Run the game using the command: python tictactoe.py
The game will display the TicTacToe board with numbers representing the positions.
Follow the on-screen instructions to play the game:
Enter the number (0-8) where you want to place your "O" character.
The opponent (playing as "X") will make a random move after your turn.
The game continues until a player wins, loses, or the game ends in a draw.

Game Rules
Players take turns placing their characters ("O" for the player and "X" for the AI) on the 3x3 grid.
The player wins if they have three of their characters in a row (horizontally, vertically, or diagonally).
The game ends in a draw if all positions on the board are filled and there is no winner.

Code Overview
The tictactoe.py script contains the following functions:
printing(table): Prints the current state of the TicTacToe board.
showBoard(): Displays the positions on the board with numbers for reference.
ai(table): Implements the AI's random move by selecting an available position.
winning(table): Checks for a win condition (three characters in a row for "O" or "X").
draw(table): Draws a empty board.
game(table): Main game loop that allows players to take turns and checks for win/draw conditions.
Customize and Improve
Feel free to modify and enhance the game to add more features, improve AI logic, or create a graphical interface. Some possible improvements include:

Enjoy playing the game and experimenting with the code!


