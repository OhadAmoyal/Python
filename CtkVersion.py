import customtkinter
import random
import time

defult_difficulty = 'pro'
last_difficulty = 'AI'
generating = False
game_mode = None


def generate_row():
    return random.randint(0, 2)


def generate_col():
    return random.randint(0, 2)


def check_winner(color="green"):
    global x_score, o_score  # Assuming x_score and o_score are used elsewhere

    # Check rows for a win
    for row in range(3):
        if (buttons[row][0].cget('text') == buttons[row][1].cget('text') == buttons[row][2].cget('text') != ""):
            if not generating:
                # Set color for the winning cells
                for col in range(3):
                    buttons[row][col].configure(fg_color=color, hover_color="dark green")
            else:
                # Set color for generating mode
                for col in range(3):
                    buttons[row][col].configure(fg_color=color, hover_color=color)
            return True

    # Check columns for a win
    for col in range(3):
        if (buttons[0][col].cget('text') == buttons[1][col].cget('text') == buttons[2][col].cget('text') != ""):
            if not generating:
                # Set color for the winning cells
                for row in range(3):
                    buttons[row][col].configure(fg_color=color, hover_color="dark green")
            else:
                # Set color for generating mode
                for row in range(3):
                    buttons[row][col].configure(fg_color=color, hover_color=color)
            return True

    # Check diagonals for a win
    if (buttons[0][0].cget('text') == buttons[1][1].cget('text') == buttons[2][2].cget('text') != ""):
        if not generating:
            # Set color for the winning cells
            for i in range(3):
                buttons[i][i].configure(fg_color=color, hover_color="dark green")
        else:
            # Set color for generating mode
            for i in range(3):
                buttons[i][i].configure(fg_color=color, hover_color=color)
        return True

    elif (buttons[0][2].cget('text') == buttons[1][1].cget('text') == buttons[2][0].cget('text') != ""):
        if not generating:
            # Set color for the winning cells
            for i in range(3):
                buttons[i][2 - i].configure(fg_color=color, hover_color="dark green")
        else:
            # Set color for generating mode
            for i in range(3):
                buttons[i][2 - i].configure(fg_color=color, hover_color=color)
        return True

    elif empty_spaces() is False:
        # If the board is full and no winner, it's a draw
        for row in range(3):
            for col in range(3):
                if not generating:
                    buttons[row][col].configure(fg_color="red", hover_color="dark red")
                else:
                    buttons[row][col].configure(fg_color="red", hover_color="red")
        return "draw"
    else:
        return False


def who_won():
    for row in range(3):
        if (buttons[row][0].cget("text") == buttons[row][1].cget("text") == buttons[row][2].cget("text") == players[0]):
            return players[0]

    for col in range(3):
        if (buttons[0][col].cget("text") == buttons[1][col].cget("text") == buttons[2][col].cget("text") == players[0]):
            return players[0]

    if (buttons[0][0].cget("text") == buttons[1][1].cget("text") == buttons[2][2].cget("text") == players[0]):
        return players[0]

    elif (buttons[0][2].cget("text") == buttons[1][1].cget("text") == buttons[2][0].cget("text") == players[0]):
        return players[0]

    for row in range(3):
        if (buttons[row][0].cget("text") == buttons[row][1].cget("text") == buttons[row][2].cget("text") == players[1]):
            return players[1]

    for col in range(3):
        if (buttons[0][col].cget("text") == buttons[1][col].cget("text") == buttons[2][col].cget("text") == players[1]):
            return players[1]

    if (buttons[0][0].cget("text") == buttons[1][1].cget("text") == buttons[2][2].cget("text") == players[1]):
        return players[1]

    elif (buttons[0][2].cget("text") == buttons[1][1].cget("text") == buttons[2][0].cget("text") == players[1]):
        return players[1]

    if empty_spaces() is False:
        return "draw"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if buttons[row][col].cget("text") != "":
                spaces -= 1

    return spaces != 0


def new_game():
    global player, o_score, x_score, draw_score

    # Resetting difficulty button colors
    for button in difficulty:
        button.configure(fg_color=['#3a7ebf', '#1f538d'])

    # Highlight selected difficulty level
    selected_difficulty = get_difficulty()
    if selected_difficulty == "noob":
        difficulty[0].configure(fg_color="blue")
    elif selected_difficulty == "pro":
        difficulty[1].configure(fg_color="red")
    elif selected_difficulty == "AI":
        difficulty[2].configure(fg_color="#7F609D")

    # Update score label
    score_label.configure(text="wins:" + str(x_score) + " loses:" + str(o_score) + " draws:" + str(int(draw_score)))

    # Reset game state
    player = players[0]
    label.configure(text="your turn")

    # Clear the game board buttons
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(text="", fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])


def set_difficulty(col):
    global defult_difficulty, last_difficulty
    last_difficulty = defult_difficulty
    defult_difficulty = difficulty[col].cget("text")

    # Update difficulty button colors based on selection
    if col == 0:
        difficulty[0].configure(fg_color="blue", hover_color="dark blue")
        difficulty[1].configure(fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])
        difficulty[2].configure(fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])

    if col == 1:
        difficulty[0].configure(fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])
        difficulty[1].configure(fg_color="red", hover_color="dark red")
        difficulty[2].configure(fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])

    if col == 2:
        difficulty[0].configure(fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])
        difficulty[1].configure(fg_color=['#3a7ebf', '#1f538d'], hover_color=['#325882', '#14375e'])
        difficulty[2].configure(fg_color="#7F609D", hover_color="purple")

    # Restore previous color for generating mode
    if generating:
        if difficulty[0].cget("text") == get_last_difficulty():
            difficulty[0].configure(fg_color="blue", hover_color='dark blue')
        if difficulty[1].cget("text") == get_last_difficulty():
            difficulty[1].configure(fg_color="red", hover_color="dark red")
        if difficulty[2].cget("text") == get_last_difficulty():
            difficulty[2].configure(fg_color="#7F609D", hover_color='purple')


def get_difficulty():
    global defult_difficulty
    return defult_difficulty


def get_last_difficulty():
    global last_difficulty
    return last_difficulty


def next_turn(row, col):
    global player, x_score, o_score, draw_score

    # Check if the selected cell is empty and no winner
    if buttons[row][col].cget('text') == "" and check_winner() is False:
        # Handle player's turn
        buttons[row][col].configure(text=player)

        # Check if player did not win
        if check_winner() is False:
            player = players[1]
            label.configure(text=(get_difficulty() + " turn"))
            window.update()
            time.sleep(.8)

            # Handle PC's turn
            pc_turn(get_difficulty())

            # Check if PC won
            if check_winner() is True:
                o_score += 1
                score_label.configure(
                    text="wins:" + str(x_score) + " loses:" + str(o_score) + " draws:" + str(int(draw_score)))
                return

        # Player wins
        if check_winner() is True:
            if not generating:
                label.configure(text=("you won"))
            if generating:
                label.configure(text=(get_difficulty() + " won"))
            x_score += 1
            score_label.configure(
                text="wins:" + str(x_score) + " loses:" + str(o_score) + " draws:" + str(int(draw_score)))

        # Draw
        if check_winner() == "draw":
            label.configure(text="draw")
            draw_score += 1
            score_label.configure(
                text="wins:" + str(x_score) + " loses:" + str(o_score) + " draws:" + str(int(draw_score)))


def pc_turn(difficulty):
    global player

    # Perform different moves based on difficulty
    if difficulty == 'noob':
        random_move(player)

    elif difficulty == 'pro':
        good_move(player)

    elif difficulty == 'AI':
        best_move()

    # Update game state after PC's turn
    if check_winner() is False:
        player = players[0]

        # Update label based on generating mode
        if generating:
            label.configure(text=(get_last_difficulty() + " turn"))
        else:
            label.configure(text=("your turn"))

    # PC wins
    elif check_winner() is True:
        if not generating:
            label.configure(text=("you lost"))
        if generating:
            label.configure(text=(get_difficulty() + " won"))

    # Draw
    elif check_winner() == "draw":
        label.configure(text="draw")


def random_move(player):
    # insert in random cell
    insert = False
    while not insert:
        row = generate_row()
        col = generate_col()
        if buttons[row][col].cget("text") == "":
            buttons[row][col].configure(text=player)
            insert = True


def good_move(player):
    # Try to block opponent's winning move or find a winning move
    inserted = False
    # Try to find winning move
    for row in range(3):
        for col in range(3):
            if buttons[row][col].cget("text") == "" and not inserted:
                buttons[row][col].configure(text=player)
                if who_won() is not False:
                    inserted = True
                if who_won() is False:
                    buttons[row][col].configure(text="")

    # Try to block opponent's
    for row in range(3):
        for col in range(3):
            if buttons[row][col].cget("text") == "" and not inserted:
                if player == players[1]:
                    buttons[row][col].configure(text=players[0])
                if player == players[0]:
                    buttons[row][col].configure(text=players[1])
                if who_won() is not False and inserted == False:
                    buttons[row][col].configure(text=player)
                    inserted = True
                elif who_won() is False:
                    buttons[row][col].configure(text="")

    # If no strategic moves, make a random move
    if inserted == False:
        random_move(player)



def best_move():
    if player == players[0]:
        other_player = players[1]
    elif player == players[1]:
        other_player = players[0]

    # Before we use the minimax algorithm we'll check the status of the board for quick insertions
    AI_started = False

    # Check if the board is empty
    if (buttons[0][0].cget('text') == buttons[0][1].cget('text') == buttons[0][2].cget('text') ==
            buttons[1][0].cget('text') == buttons[1][1].cget('text') == buttons[0][2].cget('text') ==
            buttons[2][0].cget('text') == buttons[2][1].cget('text') == buttons[2][2].cget('text') == ''):
        # Place AI's piece in one of the corners
        buttons[random.randrange(0, 3, 2)][random.randrange(0, 3, 2)].configure(text=player)
        AI_started = True
        return

    # If the center is available, place AI's piece there
    if not (buttons[0][0].cget('text') == buttons[0][1].cget('text') == buttons[0][2].cget('text') ==
            buttons[1][0].cget('text') == buttons[1][1].cget('text') == buttons[0][2].cget('text') ==
            buttons[2][0].cget('text') == buttons[2][1].cget('text') == buttons[2][2].cget('text') == ''):
        if buttons[1][1].cget('text') == '':
            if not AI_started:
                buttons[1][1].configure(text=player)
                return

    # If only center is taken, Place AI's piece in one of the corners
    if (buttons[0][0].cget('text') == buttons[0][1].cget('text') == buttons[0][2].cget('text') ==
        buttons[1][0].cget('text') == buttons[1][2].cget('text') ==
        buttons[2][0].cget('text') == buttons[2][1].cget('text') == buttons[2][2].cget('text') == '') and buttons[1][
        1].cget('text') != '':
        buttons[random.randrange(0, 3, 2)][random.randrange(0, 3, 2)].configure(text=player)
        return

    # Use the minimax algorithm to find the best move
    best_score = -float('inf')
    best_row = None
    best_col = None
    for row in range(3):
        for col in range(3):
            if buttons[row][col].cget('text') == '':
                buttons[row][col].configure(text=player)
                score = minimax(buttons, 0, False)
                buttons[row][col].configure(text='')
                if score > best_score:
                    best_score = score
                    best_row = row
                    best_col = col
    buttons[best_row][best_col].configure(text=player)



def minimax(buttons, depth, is_maximizing):
    # Determine the other player based on the current player
    if player == players[0]:
        other_player = players[1]
    elif player == players[1]:
        other_player = players[0]

    # Check for terminal game states (win, lose, draw)
    if who_won() == other_player:
        return -10 + depth
    if who_won() == player:
        return 10 - depth
    if who_won() == "draw":
        return 0

    # If maximizing player's turn
    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if buttons[row][col].cget('text') == "":
                    buttons[row][col].configure(text=player)
                    score = minimax(buttons, depth + 1, False)
                    buttons[row][col].configure(text='')
                    best_score = max(score, best_score)
        return best_score
    # If minimizing player's turn
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if buttons[row][col].cget('text') == "":
                    buttons[row][col].configure(text=other_player)
                    score = minimax(buttons, depth + 1, True)
                    buttons[row][col].configure(text='')
                    best_score = min(score, best_score)
        return best_score



def set_generating():
    global generating
    generating = True



def get_opp():
    global generating

    # Display buttons frame
    buttons_frame.pack()

    # Grid layout for buttons
    for row in range(3):
        for col in range(3):
            buttons[row][col].grid(row=row, column=col)

    # Update the window
    window.update()

    # Map last difficulty to an index
    if get_last_difficulty() == difficulty[0].cget("text"):
        x = 0
    elif get_last_difficulty() == difficulty[1].cget("text"):
        x = 1
    elif get_last_difficulty() == difficulty[2].cget("text"):
        x = 2

    # Map current difficulty to an index
    if get_difficulty() == difficulty[0].cget("text"):
        o = 0
    elif get_difficulty() == difficulty[1].cget("text"):
        o = 1
    elif get_difficulty() == difficulty[2].cget("text"):
        o = 2

    # Generate the game based on the mapped difficulties
    generate_game(x, o)


def generate_game(x, o):
    global player, x_score, o_score, draw_score, generating

    window.update()
    # Update score label based on difficulties and scores
    score_label.configure(
        text=difficulty[x].cget("text") + ":" + str(x_score) + " " + difficulty[o].cget("text") + ":" + str(
            o_score) + " draws:" + str(int(draw_score)))
    # Check if the game already ended
    if check_winner() is not False:
        new_generate(x, o)

    # Continue generating the game
    if check_winner() is False:
        # Update UI to show generating progress
        generate_button.configure(text="generating")
        if player == players[0]:
            pc_turn(difficulty[x].cget("text"))

            if check_winner() is False:
                # Update UI to show generating progress
                generate_button.configure(text="generating.")
                window.update()
                player = players[1]
                # Update UI to show generating progress
                label.configure(text=(get_difficulty() + " turn"))
                window.update()
                time.sleep(.4)
                # Update UI to show generating progress
                generate_button.configure(text="generating..")
                window.update()
                time.sleep(.4)
                # Update UI to show generating progress
                generate_button.configure(text="generating...")
                pc_turn(difficulty[o].cget("text"))
                window.update()
                time.sleep(.4)
                # Update UI to show generating progress
                generate_button.configure(text="generating....")
                window.update()
                time.sleep(.4)
                generate_button.configure(text="generating...")
                window.update()
                if check_winner() is True:
                    o_score += 1
                    score_label.configure(
                        text=difficulty[x].cget("text") + ":" + str(x_score) + " " + difficulty[o].cget(
                            "text") + ":" + str(o_score) + " draws:" + str(int(draw_score)))
                    generate_button.configure(text="generate a new game")
                    return

            if check_winner() is True:
                label.configure(text=(difficulty[x].cget("text") + " wins"))
                x_score += 1
                score_label.configure(
                    text=difficulty[x].cget("text") + ":" + str(x_score) + " " + difficulty[o].cget(
                        "text") + ":" + str(o_score) + " draws:" + str(int(draw_score)))
                generate_button.configure(text="generate a new game")

            if check_winner() is False:
                generate_game(x, o)

            if check_winner() == "draw":
                label.configure(text="draw")
                draw_score += 0.2
                score_label.configure(
                    text=difficulty[x].cget("text") + ":" + str(x_score) + " " + difficulty[o].cget(
                        "text") + ":" + str(o_score) + " draws:" + str(int(draw_score)))
                generate_button.configure(text="generate a new game")



def new_generate(x, o):
    global player

    window.update()

    # Update score label based on difficulties and scores
    score_label.configure(
        text=difficulty[x].cget("text") + ":" + str(x_score) + " " + difficulty[o].cget(
            "text") + ":" + str(o_score) + " draws:" + str(int(draw_score)))

    # Reset player and label
    player = players[0]
    label.configure(text=get_last_difficulty() + " turn")

    # Clear the buttons and reset their appearance
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(text="", fg_color=['#3a7ebf', '#1f538d'], hover_color=['#3a7ebf', '#1f538d'])

# Set up customtkinter appearance mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window
window = customtkinter.CTk()
window.geometry("500x600+570+0")
window.title("Tic Tac Toe")

# Initialize game variables
players = ["x", "o"]
player = players[0]
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

difficulty = [0, 0, 0]
x_score = 0
o_score = 0
draw_score = 0

# Create game mode selection labels and buttons
game_mode_label = customtkinter.CTkLabel(master=window, text="select game mode", font=('consolas', 50))
game_mode_label.pack(pady=100)

human_pc_button = customtkinter.CTkButton(master=window, text="play a game", font=('consolas', 20), width=200,
                                          height=100, border_width=1, border_color="black",
                                          command=lambda gamemode="human": set_game_mode(gamemode))
human_pc_button.pack(side='left', padx=20)

pc_pc_button = customtkinter.CTkButton(master=window, text="watch a game", font=('consolas', 20), width=200,
                                       height=100, border_width=1, border_color="black",
                                       command=lambda gamemode="pc": set_game_mode(gamemode))
pc_pc_button.pack(side='right', padx=20)

# Create label for current player's turn or game status
if generating:
    label = customtkinter.CTkLabel(master=window, text=get_last_difficulty() + " turn", font=('consolas', 40))
else:
    label = customtkinter.CTkLabel(master=window, text="start playing", font=('consolas', 40))

# Create label to display scores
score_label = customtkinter.CTkLabel(master=window,
                                     text="wins:" + str(x_score) + " loses:" + str(o_score) + " draws:" + str(
                                         draw_score),
                                     font=('consolas', 15))

# Create frame for difficulty buttons
difficulty_frame = customtkinter.CTkFrame(master=window)

# Create difficulty selection buttons
for col, diff_text in enumerate(["noob", "pro", "AI"]):
    difficulty[col] = customtkinter.CTkButton(master=difficulty_frame, text=diff_text, font=('consolas', 20),
                                              width=100, height=10, border_width=1, border_color="black",
                                              fg_color="red" if diff_text == "pro" else None,
                                              hover_color="dark red" if diff_text == "pro" else None,
                                              command=lambda col=col: set_difficulty(col))
    difficulty[col].grid(row=0, column=col)

# Create restart button
reset_button = customtkinter.CTkButton(master=window, text="restart", font=('consolas', 20), width=300,
                                       height=40, border_width=1, border_color="black", command=new_game)

# Create frame for game buttons
buttons_frame = customtkinter.CTkFrame(master=window)

# Create game buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = customtkinter.CTkButton(master=buttons_frame, text="", font=('consolas', 40),
                                                    width=100, height=100, corner_radius=0, border_width=1,
                                                    border_color="black",
                                                    command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

# Create button for generating a game
generate_button = customtkinter.CTkButton(master=window, text="generate a game", font=('consolas', 20),
                                          width=300, height=40, border_width=1, border_color="black",
                                          command=get_opp)

# Define function for the first window
def first_window():
    global generating

    for widget in window.winfo_children():
        widget.destroy()

    generating = False

    game_mode_label = customtkinter.CTkLabel(master=window, text="select game mode", font=('consolas', 50))
    game_mode_label.pack(pady=100)

    human_pc_button = customtkinter.CTkButton(master=window, text="play a game", font=('consolas', 20), width=200,
                                              height=100, border_width=1, border_color="black",
                                              command=lambda gamemode="human": set_game_mode(gamemode))
    human_pc_button.pack(side='left', padx=20)

    pc_pc_button = customtkinter.CTkButton(master=window, text="watch a game", font=('consolas', 20), width=200,
                                           height=100, border_width=1, border_color="black",
                                           command=lambda gamemode="pc": set_game_mode(gamemode))
    pc_pc_button.pack(side='right', padx=20)

# Define function for the second window
def set_game_mode(gamemode):
    global game_mode, players, player, difficulty, x_score, o_score, draw_score, label, score_label, difficulty_frame, reset_button, buttons_frame, generate_button, generating
    game_mode = gamemode
    x_score = 0
    o_score = 0
    draw_score = 0

    for widget in window.winfo_children():
        widget.destroy()

    if game_mode == "human":

        label = customtkinter.CTkLabel(master=window, text="start playing", font=('consolas', 40))

        label.pack(pady=20, padx=2)

        score_label = customtkinter.CTkLabel(master=window,
                                             text="wins:" + str(x_score) + " loses:" + str(o_score) + " draws:" + str(
                                                 draw_score),
                                             font=('consolas', 15))
        score_label.pack()

        difficulty_frame = customtkinter.CTkFrame(master=window)
        difficulty_frame.pack()

        difficulty[0] = customtkinter.CTkButton(master=difficulty_frame, text="noob", font=('consolas', 20), width=100,
                                                height=10, border_width=1, border_color="black",
                                                command=lambda col=0: set_difficulty(col))
        difficulty[0].grid(row=0, column=0)
        difficulty[1] = customtkinter.CTkButton(master=difficulty_frame, text="pro", font=('consolas', 20), width=100,
                                                height=10, border_width=1, border_color="black", fg_color="red",
                                                hover_color="dark red",
                                                command=lambda col=1: set_difficulty(col))
        difficulty[1].grid(row=0, column=1)
        difficulty[2] = customtkinter.CTkButton(master=difficulty_frame, text="AI", font=('consolas', 20), width=100,
                                                height=10, border_width=1, border_color="black",
                                                command=lambda col=2: set_difficulty(col))
        difficulty[2].grid(row=0, column=2)

        reset_button = customtkinter.CTkButton(master=window, text="restart", font=('consolas', 20), width=300,
                                               height=40, border_width=1, border_color="black", command=new_game)
        reset_button.pack()

        buttons_frame = customtkinter.CTkFrame(master=window)
        buttons_frame.pack()

        for row in range(3):
            for col in range(3):
                buttons[row][col] = customtkinter.CTkButton(master=buttons_frame, text="", font=('consolas', 40),
                                                            width=100, height=100, corner_radius=0, border_width=1,
                                                            border_color="black",
                                                            command=lambda row=row, col=col: next_turn(row, col))
                buttons[row][col].grid(row=row, column=col)

        switch_game_mode_button = customtkinter.CTkButton(master=window, text="switch game mode",
                                                          font=('consolas', 20), width=300, height=40,
                                                          border_width=1, border_color="black",
                                                          command=first_window)
        switch_game_mode_button.pack(side='bottom', pady=40)

    if game_mode == "pc":

        generating = True

        label = customtkinter.CTkLabel(master=window, text="select 2 " + "\n" + "difficulties", font=('consolas', 50))
        label.pack(pady=20, padx=2)

        score_label = customtkinter.CTkLabel(master=window,
                                             text="",
                                             font=('consolas', 15))
        score_label.pack()

        difficulty_frame = customtkinter.CTkFrame(master=window)
        difficulty_frame.pack()

        difficulty[0] = customtkinter.CTkButton(master=difficulty_frame, text="noob", font=('consolas', 20), width=100,
                                                height=10, border_width=1, border_color="black",
                                                command=lambda col=0: set_difficulty(col))
        difficulty[0].grid(row=0, column=0)
        difficulty[1] = customtkinter.CTkButton(master=difficulty_frame, text="pro", font=('consolas', 20), width=100,
                                                height=10, border_width=1, border_color="black", fg_color="red",
                                                hover_color="dark red",
                                                command=lambda col=1: set_difficulty(col))
        difficulty[1].grid(row=0, column=1)
        difficulty[2] = customtkinter.CTkButton(master=difficulty_frame, text="AI", font=('consolas', 20), width=100,
                                                height=10, border_width=1, border_color="black", fg_color="#7F609D",
                                                hover_color="purple",
                                                command=lambda col=2: set_difficulty(col))
        difficulty[2].grid(row=0, column=2)

        generate_button = customtkinter.CTkButton(master=window, text="start", font=('consolas', 20),
                                                  width=300, height=40, border_width=1, border_color="black",
                                                  command=get_opp)
        generate_button.pack()

        buttons_frame = customtkinter.CTkFrame(master=window)

        for row in range(3):
            for col in range(3):
                buttons[row][col] = customtkinter.CTkButton(master=buttons_frame, text="", font=('consolas', 40),
                                                            width=100, height=100, corner_radius=0, border_width=1,
                                                            border_color="black", hover_color=['#3a7ebf', '#1f538d'],
                                                            command=lambda row=row, col=col: next_turn(row, col))

        switch_game_mode_button = customtkinter.CTkButton(master=window, text="switch game mode",
                                                          font=('consolas', 20), width=300, height=40,
                                                          border_width=1, border_color="black",
                                                          command=first_window)
        switch_game_mode_button.pack(side='bottom', pady=30)


window.mainloop()



