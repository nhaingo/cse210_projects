'''W01 ASSIGNMENT - HAINGOTIANA N RAMBIKARISON
TIC TAc TOE GAME'''

def main():
#Create a list of list ([1,2,3], [4,5,6], [7,8,9]) that will be stored in a variable called grill
    player1 = "X"
    player2 = "O"
    player_turn = current_player('', player1, player2)
    grill = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    display_grill(grill)
    #while there is no wiinner or the grill slot is not drawn, keep playing and display grill
    # continue with the next player
    #display grill until condition for winning game is met
    # if there is a winner print message
    player_input(player_turn, grill)
    
    while not (check_winner(grill) or slot_taken(grill, player1, player2)):
        display_grill(grill)
        player_input(player_turn, grill) 
        current_player('_', player1, player2)
    display_grill(grill)
    while (check_winner(grill)) == True:
        print("We have a win! Game is Over! Thanks for playing")
        break

# Create a board by calling the function display_grill that takes one parameter grill
# Create 3 rows with 3 slots each using a for in loop to iterate through each row of number in the list
# Iterate each element inside the list to create slots.
def display_grill(grill):
    for row in grill:
        for slot in row:
            print(f"{slot} | ", end="")
        print()
        print()
# Define the function current_player that takes three parameters: current, player1 and player2 (==> toggle player)
#Return X if ' ' or player 2, and return O if player 1
def current_player(current, player1, player2):
    if current == "" or current == player2:
        return player1
    elif current == player1:
        return player2
#Prompt user to input an integer. The number to choose is one of the number displayed in the grill (==> make a move)
#Call the function player_input that takes two parameters: player_turn, gri1ll
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
#Call the function slot_taken that takes 3 parameters: Grill, player1, player2. Iterate through the grill number if the number of the slot is taken. 
#If slot is taken return False. The function returns True as long as the slot is not taken. 
def slot_taken(grill, player1, player2):
    for row in grill:
        for slot in row:
            if slot != player1 and slot != player2:
                return False
    return True

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