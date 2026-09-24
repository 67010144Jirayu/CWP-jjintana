def checkmate(text):
    if not isinstance(text, str):
        print("Error")
        return


    board = text.splitlines()
    size = len(board)

    if size == 0 or text.count("K") != 1:
        print("Error")
        return

    for row in range(size):
        if len(board[row]) != size:
            print("Error")
            return

        if "K" in board[row]:
            king_row = row
            king_col = board[row].index("K")

    row = king_row + 1

    for col in [king_col - 1, king_col + 1]:
        if row < size and 0 <= col < size:
            if board[row][col] == "P":
                print("Success")
                return

    directions = [
        (-1,  0, "RQ"), 
        ( 1,  0, "RQ"), 
        ( 0, -1, "RQ"), 
        ( 0,  1, "RQ"),  
        (-1, -1, "BQ"),  
        (-1,  1, "BQ"),  
        ( 1, -1, "BQ"),  
        ( 1,  1, "BQ")   
    ]

    for row_step, col_step, enemy in directions:
        row = king_row + row_step
        col = king_col + col_step

        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]

            if piece in enemy:
                print("Success")
                return

            if piece in "PBRQK":
                break
              
            row += row_step
            col += col_step
          
    print("Fail")
