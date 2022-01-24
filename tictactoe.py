'''W01 ASSIGNMENT - HAINGOTIANA N RAMBIKARISON
TIC TAc TOE GAME'''

def main():
#Create a list of list that will be stored in a variable called grill
    grill = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    player1 = "X"
    player2 = "O"
    display_grill(grill)
    while not (is_winner(board) or is_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 
    player_turn = current_player('_', player1, player2)
    player_input(player_turn, grill)
    check_winner(grill)

   
# Create a board by calling the function display_grill that takes one parameter grill
# Create 3 rows with 3 slots each using a for in loop to iterate through each row of number in the list.add()
# Iterate each element of the inside the list.
def display_grill(grill):
    for row in grill:
        for slot in row:
            print(f"{slot} | ", end="")
        print()
        print()
#Define the function current_player that takes three parameters: current, player1 and player2
def current_player(current, player1, player2):
    if current == "" or current == player2:
        return player1
    elif current == player1:
        return player2
#Prompt user to input an integer. The number to choose is one of the number displayed in the grill
#Call the function player_input that takes two parameters: player_turn, grill
#Use if statement to compare number from input with the number on the grill. The function should replace the number on the grill with X or O from the function current_player() 
def player_input(player_turn, grill):
    number = int(input(f"Player {player_turn}, input a number from the board (1 - 9): ")) 
    if grill[0][0] == number:
        grill[0][0] = player_turn
    elif grill[0][1] == number:
        grill[0][1] = player_turn
    elif grill[0][2] == number:
        grill[0][2] = player_turn
    elif grill[1][0] == number:
        grill[1][0] = player_turn
    elif grill[1][1] == number:
        grill[1][1] = player_turn
    elif grill[1][2] == number:
        grill[1][2] = player_turn
    elif grill[2][0] == number:
        grill[2][0] = player_turn
    elif grill[2][1] == number:
        grill[2][1] = player_turn
    elif grill[2][2] == number:
        grill[2][2] = player_turn
    else:
        return False
# call the function check_winner that pass one parameter grill and return comparisons of elements of the grill as value.
def check_winner(grill):
    return (grill[0][0] == grill[0][1] == grill[0][2] or
            grill[1][0] == grill[1][1] == grill[1][2] or
            grill[2][0] == grill[2][1] == grill[2][2] or
            grill[0][0] == grill[1][0] == grill[2][0] or
            grill[0][1] == grill[1][1] == grill[2][1] or
            grill[0][2] == grill[1][2] == grill[2][2] or
            grill[0][0] == grill[1][1] == grill[2][2] or
            grill[0][2] == grill[1][1] == grill[2][0])
            



if __name__ == "__main__":
        main()   