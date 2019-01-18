from board import Board

if __name__ == "__main__":
    game = Board(100, 0)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    print("")
    game.check_node(9, 9)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 7)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 6)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 5)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 3)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 2)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 1)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(9, 0)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(8, 7)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(8, 3)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(8, 2)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(7, 6)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(7, 5)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    game.check_node(7, 4)
    array = ""
    for i in range(10):
        array += "\n"
        for j in range(10):
            if game.board[i][j].basin:
                array += "K"
            elif game.board[i][j].visited:
                #array[i].append(game.board[i][j].adjacent)
                array += str(game.board[i][j].adjacent)
            else:
                #array[i].append(9)
                array += "#"
    print(array)
    for i in range(10):
        for j in range(10):
            if game.board[i][j].basin and game.board[i][j].visited:
                print("lose")
