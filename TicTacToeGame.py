from numpy import *


def rotate_and_mirror(board, list_of_boards):
    rotated_board_array = array([['.', '.', '.'],
                                 ['.', '.', '.'],
                                 ['.', '.', '.']])

    for i in range(3):
        for i1 in range(3):
            tuple_element = board[i][i1]
            rotated_board_array[i][i1] = tuple_element

    list_of_boards.append(rotated_board_array)

    mirror_board = array([['.', '.', '.'],
                          ['.', '.', '.'],
                          ['.', '.', '.']])

    for i in range(3):
        left_element = board[i][0]
        right_element = board[i][2]
        mirror_board[i][0] = right_element
        mirror_board[i][1] = board[i][1]
        mirror_board[i][2] = left_element

    list_of_boards.append(mirror_board)

    return board


class TicTacToeGame:
    def __init__(self, s0=None):
        if s0 is None:
            s0 = [array([['.', '.', '.'],
                         ['.', '.', '.'],
                         ['.', '.', '.']]), 1, [1, 1]]
        self.s = s0

    def which_player_turn(self):
        if self.s[1] == 1:
            return "max"
        else:
            return "min"

    def heuristic_evaluation(self):
        player_1_score = 0
        player_2_score = 0
        for i in range(3):
            for i1 in range(3):
                if i == 1 and i1 == 1:
                    if self.s[0][i][i1] == 'X':
                        player_1_score += 4
                    if self.s[0][i][i1] == 'O':
                        player_2_score += 4
                elif (i == 0 and i1 == 0) or (i == 2 and i1 == 0) or (i == 0 and i1 == 2) or (i == 2 and i1 == 2):
                    if self.s[0][i][i1] == 'X':
                        player_1_score += 3
                    if self.s[0][i][i1] == 'O':
                        player_2_score += 3
                else:
                    if self.s[0][i][i1] == 'X':
                        player_1_score += 2
                    if self.s[0][i][i1] == 'O':
                        player_2_score += 2

        return [player_1_score - player_2_score, self.s[2]]

    def check_if_terminal_state(self, depth):
        for i in range(3):
            if self.s[0][i][0] == self.s[0][i][1] and self.s[0][i][0] == self.s[0][i][2] and self.s[0][i][0] != '.':
                if self.s[0][i][0] == 'X':
                    return [1000 + depth, self.s[2]]
                else:
                    return [-1000 - depth, self.s[2]]

            if self.s[0][0][i] == self.s[0][1][i] and self.s[0][0][i] == self.s[0][2][i] and self.s[0][0][i] != '.':
                if self.s[0][0][i] == 'X':
                    return [1000 + depth, self.s[2]]
                else:
                    return [-1000 - depth, self.s[2]]

        if self.s[0][0][0] == self.s[0][1][1] and self.s[0][0][0] == self.s[0][2][2] and self.s[0][0][0] != '.':
            if self.s[0][0][0] == 'X':
                return [1000 + depth, self.s[2]]
            else:
                return [-1000 - depth, self.s[2]]

        if self.s[0][0][2] == self.s[0][1][1] and self.s[0][0][2] == self.s[0][2][0] and self.s[0][0][2] != '.':
            if self.s[0][0][2] == 'X':
                return [1000 + depth, self.s[2]]
            else:
                return [-1000 - depth, self.s[2]]

        for i1 in range(3):
            for i2 in range(3):
                if self.s[0][i1][i2] == '.':
                    return 0

        return [0, self.s[2]]

    def make_move(self, move_id):
        if self.s[1] == 1:
            player_character = 'X'
            self.s[1] = 2
        else:
            player_character = 'O'
            self.s[1] = 1

        self.s[0][move_id[0]][move_id[1]] = player_character
        self.s[2] = move_id

        if self.check_if_terminal_state(0) != 0:
            return 0

    def show_game(self):
        for i in range(3):
            print('|', self.s[0][i][0], '|', self.s[0][i][1], '|', self.s[0][i][2], '|')

    def possible_moves_all(self):
        list_possible_moves = []

        if self.s[1] == 1:
            player_character = 'X'
            new_player_turn = 2
        else:
            player_character = 'O'
            new_player_turn = 1

        for i in range(3):
            for i1 in range(3):
                if self.s[0][i][i1] == '.':
                    new_last_move = [i, i1]
                    new_board = self.s[0].copy()
                    new_board[i][i1] = player_character
                    new_s = (new_board, new_player_turn, new_last_move)
                    list_possible_moves.append(new_s)

        return list_possible_moves

    def possible_moves_symmetrical(self):

        list_possible_moves = []

        if self.s[1] == 1:
            player_character = 'X'
            new_player_turn = 2
        else:
            player_character = 'O'
            new_player_turn = 1

        list_of_symmetrical_boards = []

        for i in range(3):
            for i1 in range(3):
                if self.s[0][i][i1] == '.':
                    new_last_move = [i, i1]
                    new_board = self.s[0].copy()
                    new_board[i][i1] = player_character

                    are_boards_the_same = 0
                    number_of_unique_boards = int(len(list_of_symmetrical_boards) / 8)
                    for i2 in range(number_of_unique_boards):
                        for i3 in range(8):
                            board_id = (i2 * 8) + i3
                            compare_two_boards = list_of_symmetrical_boards[board_id] == new_board
                            boards_equal = compare_two_boards.all()
                            if boards_equal:
                                are_boards_the_same = 1
                                choose_random = random.choice([1, 2])
                                if choose_random == 1:
                                    new_s = (new_board, new_player_turn, new_last_move)
                                    list_possible_moves[i2] = new_s

                    if are_boards_the_same == 0:
                        new_s = (new_board, new_player_turn, new_last_move)
                        list_possible_moves.append(new_s)

                        mirror_board = array([['.', '.', '.'],
                                              ['.', '.', '.'],
                                              ['.', '.', '.']])

                        list_of_symmetrical_boards.append(new_board)
                        for i3 in range(3):
                            left_element = new_board[i3][0]
                            right_element = new_board[i3][2]
                            mirror_board[i3][0] = right_element
                            mirror_board[i3][1] = new_board[i3][1]
                            mirror_board[i3][2] = left_element

                        list_of_symmetrical_boards.append(mirror_board)

                        rotated_board = new_board
                        for i4 in range(3):
                            rotated_board = list(zip(*rotated_board[::-1]))
                            rotate_and_mirror(rotated_board, list_of_symmetrical_boards)

        return list_possible_moves
