from random import choice

class Game():
    def __init__(self, num_turns=12):
        self.num_turns = num_turns
        self.turns_remaining = num_turns
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
        
        for i, guess in enumerate(guesses):
            if guess in self.code:
                if self.code.index(guess) == i:
                    correct_color_and_pos += 1
                else:
                    correct_color_wrong_pos += 1

        return [
            correct_color_and_pos,
            correct_color_wrong_pos
        ]

    def play_turn(self):

        if self.turns_remaining == 0:
            self.is_game_over = True
            return('Game over!')
        
        player_guess = input('Please submit a guess\n')
        player_guess_split = player_guess.split(', ')
        feedback = self.provide_feedback(player_guess_split)

        self.turns_remaining -= 1

        if feedback[0] == 4:
            self.is_game_over = True
            return f'You won in {self.num_turns - self.turns_remaining} turns!!! The code was: {(", ").join(self.code)}'

        return(f'''Turn {self.num_turns - self.turns_remaining} / {self.turns_remaining}
        In your guess you had:
        - {feedback[0]} in the correct color and position
        - {feedback[1]} in the correct color but wrong position
        ''')

        
        
