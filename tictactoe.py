class Board():
    def __init__(self):
        self.grill = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    def display_grill(self):
        for row in self.grill:
            for slot in row:
                print(f"{slot} | ", end="")
            print()
            print()
        print()
    def update_grill(self, grill_number, player1):
        def coordinates(player1):
            row = int(grill_number/3)
            col = int(grill_number/3)
            if col > 2:
                col = col % 3 
                return (col, row)
            if grill_number == self.grill[row][col]:
                self.grill = player1
        coordinates(player1)


    
         
board = Board()

while True:
    board.display_grill()
    player1_X = int(input("please enter a number 1 - 9: "))
    
    board.update_grill(player1_X, "X")
    