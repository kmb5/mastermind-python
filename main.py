from objects import Game

def main():

    game = Game()
    
    while not game.is_game_over:

        turn = game.play_turn()
        print(turn)



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