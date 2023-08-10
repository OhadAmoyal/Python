

Setting up Game Modes:

The code defines two game modes: "play" and "watch". Players can choose between playing against AI or watching two AI players compete against each other.


Creating GUI Elements:

The code uses the customtkinter library to create graphical user interface (GUI) elements for the game.


play Game Mode:

In the "play" game mode, players can play against AI.
A label displays "start playing" to indicate the beginning of the game.
The score label shows the number of wins, losses, and draws.
Difficulty buttons allow players to select the opponent skill level(noob - random moves, pro - knows how to do a winning move or a blocking move, and AI - generate all the possible sequences and choose the best move).
The "restart" button lets players start a new game.
The game board consists of a 3x3 grid of buttons, allowing players to make their moves.
The "switch game mode" button allows players to switch between game modes.


watch Game Mode:

In the "watch" game mode, players can watch two AI players compete against each other.
A label prompts players to select two difficulty levels for the AI players.
Difficulty buttons are used to select the AI's skill level(pro vs AI for defult).
The "start" button generates a game between the two AI players.
The game board layout is the same as in play mode.
The "switch game mode" button allows players to switch to the human game mode.


Functionality:

Players can select the difficulty level for the AI opponent(s) in both game modes.
The "generate" button in watch mode generates a game based on the chosen difficulties.
Game buttons allow players to interact with the game board and make moves.
The game board is a 3x3 grid of buttons where players can click to place their "x" or "o" symbol.
The game checks for winning conditions (3 in a row) or a draw condition.
The "restart" button in play mode allows players to start a new game.
The "switch game mode" button switches between the "watch" and "play" game modes.
