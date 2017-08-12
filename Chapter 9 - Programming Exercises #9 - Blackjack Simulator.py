import random

def create_deck():

    deck = {"Ace of Spades": 1, "2 of Spades" : 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades" : 5,
            "6 of Spades" : 6, "7 of Spades" : 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10,
            "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10,

            "Ace of Hearts": 1, "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5,
            "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9, "10 of Hearts": 10,
            "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10,

            "Ace of Clubs": 1, "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5,
            "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9, "10 of Clubs": 10,
            "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10,

            "Ace of Diamonds": 1, "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5,
            "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9, "10 of Diamonds": 10,
            "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10}

    return deck

def deal_cards(deck):

    p1_hand_value = 0
    p2_hand_value = 0
    card_number = 0

    win = False


    for count in range(len(deck)):
        while win == False:

            #https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-in-python-dictionary
            #That will work in Python 2.x where d.keys() is a list, but it won't work in Python 3.x where d.keys() is an iterator. You should do random.choice(list(d.keys())) instead.

            key = random.choice(list(deck.keys()))
            print("Card #", card_number + 1, "for Player 1:")
            print(key)

            if key == "Ace of Spades" or key == "Ace of Hearts" or key == "Ace of Clubs" or key == "Ace of Diamonds" and p1_hand_value < 11:
                p1_hand_value += 11
            else:
                p1_hand_value += deck[key]

            del deck[key]

            key2 = random.choice(list(deck.keys()))
            print("Card #", card_number + 1, "for Player 2:")
            print(key2)

            card_number += 1

            if key2 == "Ace of Spades" or key2 == "Ace of Hearts" or key2 == "Ace of Clubs" or key2 == "Ace of Diamonds" and p2_hand_value < 11:
                p2_hand_value += 11
            else:
                p2_hand_value += deck[key2]

            del deck[key2]

            if p1_hand_value == 21 and p2_hand_value == 21:
                print("Player 1's hand value is", p1_hand_value)
                print("Player 2's hand value is", p2_hand_value)
                print("The game is a tie")
                win = True
            elif p1_hand_value > 21 and p2_hand_value > 21:
                print("Player 1's hand value is", p1_hand_value)
                print("Player 2's hand value is", p2_hand_value)
                print("The game is a tie")
                win = True
            elif p1_hand_value > 21 or p2_hand_value == 21:
                print("Player 1's hand value is", p1_hand_value)
                print("Player 2's hand value is", p2_hand_value)
                print("Player 2 wins!")
                win = True
            elif p2_hand_value > 21 or p1_hand_value == 21:
                print("Player 1's hand value is", p1_hand_value)
                print("Player 2's hand value is", p2_hand_value)
                print("Player 1 wins!")
                win = True

def main():

    deck = create_deck()

    input("Press enter to play.")

    deal_cards(deck)

main()