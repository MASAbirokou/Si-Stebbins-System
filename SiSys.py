#!/usr/bin/env python3

# you can change these four bottom cards as you like
btm_diamonds = 4
btm_clubs = 7
btm_hearts = 10
btm_spades = 13

def from_top(index, btm_card, subtrahend):
    diff = btm_card - index if index < btm_card else (btm_card + 13) - index
    diff_4 = diff * 4
    result = diff_4 - subtrahend
    print('from top -> ', result) 

def calc(suit, index):
    if suit == 'diamonds':
        from_top(index, btm_diamonds, 3)
    elif suit == 'clubs':
        from_top(index, btm_clubs, 2)
    elif suit == 'hearts':
        from_top(index, btm_hearts, 1)
    elif suit == 'spades':
        from_top(index, btm_spades, 0)

def main():
    try:
        while True:
            suit = input('suit: ')
            index = input('index: ')
            print('--------------------')
            calc(suit, int(index))
            print('--------------------\n')

    except:
        return None

if __name__ == "__main__": 
    main()
