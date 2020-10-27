from objects import Game

def _main():

    # main alternative
    # to test
    # test

    game = Game()

    print(game.code)
    
    while not game.is_game_over:

        turn = game.play_turn()
        print(turn)

def main():

    game = Game()
    print(game.code)
    turn = [0,0,0,0]
    game.code = ['red', 'red', 'red', 'red']

    while not game.is_game_over:
        turn = game.play_turn_computer(turn)



def randdd():

    all_turns = []

    for i in range(1000):

        num_turns = 0
        correct = ''

        while correct != 4:

            game = Game()
            correct = game.provide_feedback(['red','white','blue','yellow'])[0]
            num_turns += 1

        all_turns.append(num_turns)

    print(min(all_turns))

if __name__ == "__main__":
    main()