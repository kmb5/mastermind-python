from random import choice

class Game():
    def __init__(self, num_turns=12):
        self.num_turns = num_turns
        self.turns_passed = 0
        self.is_game_over = False
        self.colors = [
            'blue',
            'yellow',
            'green',
            'orange',
            'white',
            'red']
        self.code = self.generate_code()

    def generate_code(self):

        return [choice(self.colors) for x in range(4)]

    def provide_feedback(self, guesses):

        correct_color_and_pos = 0
        correct_color_wrong_pos = 0
        
        for i, code in enumerate(self.code):
            if code in guesses:
                if guesses[i] == code:
                    correct_color_and_pos += 1
                else:
                    correct_color_wrong_pos += 1

        return [
            correct_color_and_pos,
            correct_color_wrong_pos
        ]

    def play_turn(self):

        if self.turns_passed == self.num_turns:
            self.is_game_over = True
            return(f'Game over! The code was {(", ").join(self.code)}')
        
        player_guess = input(f'Please submit a guess\nThe available colors are the following: {(", ").join(self.colors)}\n>>> ')
        player_guess_split = player_guess.split(', ')
        feedback = self.provide_feedback(player_guess_split)

        self.turns_passed += 1

        if feedback[0] == 4:
            self.is_game_over = True
            return f'You won in {self.turns_passed} turns!!! The code was: {(", ").join(self.code)}'

        return(f'''Turn {self.turns_passed} / {self.num_turns}
        In your guess you had:
        - {feedback[0]} in the correct color and position
        - {feedback[1]} in the correct color but wrong position
        ''')

    def play_turn_computer(self, prev_turn=[0,0,0,0]):

        self.turns_passed += 1

        if self.turns_passed == self.num_turns:
            self.is_game_over = True
            print(f'Game over! The code was {(", ").join(self.code)}')

        computer_guess = [
            choice(self.colors) if prev_turn[x] == 0 else prev_turn[x] for x in range(4)
            ]
        
        print(f'The computer guessed {(", ").join(computer_guess)}')
        feedback = self.provide_feedback(computer_guess)
        print(f'''Turn {self.turns_passed} / {self.num_turns}
        In your guess you had:
        - {feedback[0]} in the correct color and position
        - {feedback[1]} in the correct color but wrong position
        ''')

        if feedback[0] == 4:
            self.is_game_over = True
            print(f'The computer won in {self.turns_passed} turns!')

        for i, el in enumerate(self.code):
            if computer_guess[i] == el:
                prev_turn[i] = el

        return prev_turn




        
        
