from random import randint

def display_table(list_of_moves):

    for index in range(len(list_of_moves)):

        if list_of_moves[index] is None:
            print(" ", end="")
        else:
            print(list_of_moves[index], end="")

        if index+1 == len(list_of_moves):
            print("\n")
        elif (index + 1) % 3 == 0:
            print("\n-+-+-")
        else:
            print("|", end="")


def player_move(player):

    print("It's your turn, " + player + "\nWhere do you want to put your " + turn + "?")
    print("Line Column")
    x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1
    if move_table[x * 3 + y] is None:
        move_table[x * 3 + y] = turn
    else:
        print('Please enter a correct line and column.')
        player_move(player)


def verify_won():
    if move_table[0] == move_table[1] == move_table[2] is not None:
        return True
    elif move_table[3] == move_table[4] == move_table[5] is not None:
        return True
    elif move_table[6] == move_table[7] == move_table[8] is not None:
        return True
    elif move_table[0] == move_table[3] == move_table[6] is not None:
        return True
    elif move_table[1] == move_table[4] == move_table[7] is not None:
        return True
    elif move_table[2] == move_table[5] == move_table[8] is not None:
        return True
    elif move_table[0] == move_table[4] == move_table[8] is not None:
        return True
    elif move_table[6] == move_table[4] == move_table[2] is not None:
        return True
    return False


def robot_move():
    priority_list = [0, 2, 6, 8]
    last_priority = [1, 3, 5, 7]

    if move_table[4] is None:
        return 4
    else:
        for index in priority_list:
            if move_table[index] is None:
                return index
    for index in last_priority:
        if move_table[index] is None:
            return index

if __name__ == '__main__':
    turn = 'X'
    move_table = [None] * 9
    print("What is the player's name?")
    first_player = input()
    print("You need to write the line and column where do you want to put your X/O.\n")

    choice = randint(0, 10000)
    if choice % 2 == 1:
        first_robot = True
    else:
        first_robot = False

    if first_robot:
        print("You are the second.")
    else:
        print("You are first.")

    for i in range(9):
        display_table(move_table)
        if first_robot:
            move_table[robot_move()] = turn
            first_robot = False
        else:
            player_move(first_player)
            first_robot = True

        if i >= 5:
            if verify_won():
                display_table(move_table)
                print("Game Over!")
                print("The winner is", end=" ")

                if first_robot:
                    print(first_player)
                else:
                    print("Robot Won, try again ;)")
                exit()

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'
        display_table(move_table)



