#####################################
### WELCOME TO OOP LEARNING PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (total 10 cards). If the turned-up cards are again the same rank, each player places
# another three cards face down and one card face up. The player with the
# higher card takes all cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)


# # This is my project for learning OOP in python, I'm more focussing on the readability of
# code, I know its a very amature code, but I explained every steps just for bare beginners
# just like me, any suggestions welcome...
# Thougts on gameplay
# Developed the game with thoughts that it can be played manually as like in a reguler card gameplay
# but the problem with this game is it take enormous steps,(some time..more than 5000..plays each)
# I code it as automatic looping, you can make manual by adding simple condition in while loop..

###For beginners..
# It is not good/playable game but you can make a fun and playable game with this idea...
# just like the matchbox-card game..
# i.e simply you put your cards in the table one by one each player, when ever the two cards get the same rank,
# player with the last turn can take all the cards(whose turn matters), then alter the turn..continue till one player
# got no cards at all
# from this game you can make it easier..do that

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# Values to compare
VALUE = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.deck = []
        for suit in SUITE:
            for rank in RANKS:
                self.deck.append((suit, rank))

    def __str__(self):
        '''
        Just prints the deck
        '''
        return str(self.deck)

    def shuffle_deck(self):
        '''
        Just Shuffles the Deck
        '''
        shuffle(self.deck)

    def split_deck(self):
        '''
        Splits a shuffled deck of 52 cards equally
        and returns Two lists of cards with 26 each
        '''
        self.shuffle_deck()
        hand1 = []
        hand2 = []
        for index in range(52):   #0-51, ie 52 cards
            if index < 26:
                hand1.append(self.deck[index])
            else:
                hand2.append(self.deck[index])
        return (hand1, hand2)


class Player:
    '''
    This is the Player class. Each player has a name and a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method.
    The Player can then play cards and check if they still have cards.
    '''
    # Here the hand is a list of 26 shuffled cards from deck
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def add_card(self, cards):
        '''
        function to add card to a players hand,
        which comes from the play board as a list
        '''
        for card in cards:
            self.hand.append(card)

    def remove_card(self):
        '''
        removes the top card from the hand
        '''
        return self.hand.pop(0)

    def __str__(self):
        '''
        Just prints the hand
        '''
        return str(self.hand)

    def check_cards(self):
        '''
        Checks the hand and returns boolean
        if card exist in hand or note
        '''
        return len(self.hand) > 0

    def play_card(self, Board):
        '''
        method for playing card to the Board (adding card to the
        bord class) identifies player/system using inbuilt system Name
        '''
        if self.check_cards():
            if self.name == 'Mr X':
                Board.board['system'].append(self.remove_card())
            else:
                Board.board['player'].append(self.remove_card())
            return 1
        else:
            print("No card left to play! ")
            return 0


class Board:
    '''
    This is a sim of a playing board,
    includes
    <> clear board method
    <> take board method(takes cards from board away)
    <> display board method
    board is a Dictionary with two keys
    'player' and 'system' each associated with lists
    player playing card to the board means, card is added to the 'list'
    with 'player' key
    '''
    def __init__(self):
        self.board = {'player':[], 'system':[]}

    def take_from_board(self):
        '''
        to take all cards from the board(Dictionary) and returns it as a list
        happens if a player won a single battle/war
        '''
        board_items = []
        for card in self.board['player']:
            board_items.append(card)
        for card in self.board['system']:
            board_items.append(card)
        return board_items

    def clear_board(self):
        '''
        to clear the entire board after each single battle
        '''
        self.board['player'].clear()
        self.board['system'].clear()

    def display(self):
        '''
        to display the current board to screen
        '''
        #For the case of war, when the whole cards cannot be displayed
        if len(self.board['player']) > 1:
            print("Player:  {}, CARD1, CARD2,... {} \t Mr X:  {}, CARD1, CARD2,... {}".format(self.board['player'][0], self.board['player'][-1], self.board['system'][0], self.board['system'][-1]))

        #For a battle where player/system puts only one card in board
        else:
            print("Player:  {} \t\t\t Mr X:   {} ".format(self.board['player'], self.board['system']))



# The battle Function
def battle(g_board, player1, player2):
    '''
    Equates the rank of last card in each player's side

    if they are equal 'war' begins(calls the war function,)

    '''
    val_player_card = VALUE[g_board.board['player'][-1][1]]
    val_system_card = VALUE[g_board.board['system'][-1][1]]

    if val_player_card == val_system_card:
        war(g_board, player1, player2)

    elif val_player_card > val_system_card:
        player1.add_card(g_board.take_from_board())

    elif val_system_card > val_player_card:
        player2.add_card(g_board.take_from_board())


# Function to call when there is # WAR

def war(g_board, player1, player2):
    '''
    The war function just adds 4 more Cards
    from each side(3 face-down, last 1 face-up)
    again war calls 'battle' function(after cheking the avilability of cards) to
    look for ranks...its a kind of latching
    between these two functions until the "ranks get unequal"..
    or "cards in one player hand ends"
    '''
    for num in range(4):
        a = player1.play_card(g_board)
        b = player2.play_card(g_board)
        if a == 0 or b == 0:
            break
    g_board.display()
    if player1.check_cards() and player2.check_cards():
        battle(g_board, player1, player2)

def end_game(player1, player2):
    '''
    Just announces the winner
    '''
    print("GAME ENDS")
    #checks who is the winner(whose hand is empty)
    if player2.check_cards() == False:
        print(f"\"{player1.name}\" wins, Game ended")
    elif player1.check_cards() == False:
        print(f"\"{player2.name}\" wins, Game ended")

def show_hand_size(player1, player2):
    '''
    prints the number of cards in each players hand
    '''
    print("Player cards:  {} \t  \t Mr X cards:   {} ".format(len(player1.hand), len(player2.hand)))

######################
#### GAME PLAY #######
######################


print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
pl_name = input("Enter Your Name!: ")
print("Your opposition will be computer, 'Mr X'")

# creating game deck instance of the deck class
game_deck = Deck()

#two lists with 26 cards each for both players
hand1,hand2 = game_deck.split_deck()

#creating instance of the player class
player1 = Player(pl_name, hand1)
player2 = Player('Mr X', hand2) #computer

#Instance of the board class
game_board = Board()

#just displaying the empty game board
game_board.display()

print("You Both Got 26 cards: ")
print("Click the \"space bar\" and \"Enter\" to play your card")
gameplay = True
cycle = 0

nv = input("Enter something:")
# and input() == ' '---> for manual iteration in while loop

while gameplay:
    if player1.check_cards() and player2.check_cards():
        player1.play_card(game_board)
        player2.play_card(game_board)
        game_board.display()
        battle(game_board, player1, player2)
        show_hand_size(player1, player2)
        game_board.clear_board()
        cycle += 1
        if cycle > 3000:
            print("it's an unending Game")
            break
    else:
        print("No cards left to play, player with 0 cards gonna lose the game")
        gameplay = False
        end_game(player1, player2)
        print(f"no of cycles: {cycle}")


# Testing
# hand1 = [('S', '2'), ('H', '6'), ('D', 'Q'), ('S', '9'), ('S', 'A'), ('D', '8'), ('D', 'K'), ('H', '5')]
# hand2 = [('H', '2'), ('S', '6'), ('S', 'Q'), ('D', '9'), ('D', 'J'), ('S', '8'), ('H', 'K'), ('D', '5')]
