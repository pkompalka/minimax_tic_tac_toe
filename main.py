import TicTacToeGame
from time import *
import random


def minimax(game, depth, are_possible_moves_symmetrical):
    check_if_game_end = game.check_if_terminal_state(depth)

    if check_if_game_end != 0:
        return check_if_game_end

    if depth == 0:
        return game.heuristic_evaluation()

    if are_possible_moves_symmetrical == 1:
        list_of_possible_states = game.possible_moves_symmetrical()
    else:
        list_of_possible_states = game.possible_moves_all()

    list_of_evaluations = []

    for i in range(len(list_of_possible_states)):
        new_object = TicTacToeGame.TicTacToeGame(list_of_possible_states[i])
        new_evaluation = minimax(new_object, depth - 1, are_possible_moves_symmetrical)
        list_of_evaluations.append(new_evaluation)

    if game.which_player_turn() == "max":
        best_evaluation_value = max(list_of_evaluations, key=lambda x: x[0])[0]
    else:
        best_evaluation_value = min(list_of_evaluations, key=lambda x: x[0])[0]

    list_of_best_states = []

    for ii in range(len(list_of_evaluations)):
        if list_of_evaluations[ii][0] == best_evaluation_value:
            list_of_best_states.append(list_of_possible_states[ii])

    best_state = random.choice(list_of_best_states)

    return [best_evaluation_value, best_state[2]]


def play_game(game, depth, are_possible_moves_symmetrical):
    while True:
        game.show_game()
        start_loop_time = perf_counter()
        minimax_result = minimax(game, depth, are_possible_moves_symmetrical)
        end_loop_time = perf_counter()
        print(end_loop_time - start_loop_time)
        if minimax_result[0] > 999:
            print("Player X will always win by choosing proposed moves")
        if minimax_result[0] < -999:
            print("Player O will always win by choosing proposed moves")

        print("Best move is coordinates: ", minimax_result[1])

        if game.which_player_turn() == "max":
            user_move_x = int(input("Player X enter coordinate of field x (0, 1, 2): "))
            user_move_y = int(input("Player X enter coordinate of field y (0, 1, 2): "))
        else:
            user_move_x = int(input("Player O enter coordinate of field x (0, 1, 2): "))
            user_move_y = int(input("Player O enter coordinate of field y (0, 1, 2): "))

        user_move = [user_move_x, user_move_y]
        if game.make_move(user_move) == 0:
            game.show_game()
            print("End of game!")
            break


game_instance = TicTacToeGame.TicTacToeGame()
user_moves_symmetrical = int(input("Should list of potential moves ignore symmetric values? (1 - yes, 0 - no): "))
play_game(game_instance, 6, user_moves_symmetrical)
