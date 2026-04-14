from card_class import card
import random

class deck:
    
    
    deck_of_cards = { (1,"h"): "Ace of Hearts", (2,"h"): "Two of Hearts",(3,"h"):
    "Three of Hearts", (4,"h"): "Four of Hearts", (5,"h"): "Five of Hearts", (6,"h"): "Six of Hearts", 
    (7,"h"): "Seven of Hearts", (8,"h"): "Eight of Hearts", (9,"h"): "Nine of Hearts", (10,"h"): "Ten of Hearts"
    , (11,"h"): "Jack of Hearts", (12,"h"): "Queen of Hearts", (13,"h"): "King of Hearts",
    
    (1,"d"): "Ace of Diamonds", (2,"d"): "Two of Diamonds",(3,"d"):
    "Three of Diamonds", (4,"d"): "Four of Diamonds", (5,"d"): "Five of Diamonds", (6,"d"): "Six of Diamonds", 
    (7,"d"): "Seven of Diamonds", (8,"d"): "Eight of Diamonds", (9,"d"): "Nine of Diamonds", (10,"d"): "Ten of Diamonds"
    , (11,"d"): "Jack of Diamonds", (12,"d"): "Queen of Diamonds", (13,"d"): "King of Diamonds",
    
        (1,"c"): "Ace of Clubs", (2,"c"): "Two of Clubs",(3,"c"):
    "Three of Clubs", (4,"c"): "Four of Clubs", (5,"c"): "Five of Clubs", (6,"c"): "Six of Clubs", 
    (7,"c"): "Seven of Clubs", (8,"c"): "Eight of Clubs", (9,"c"): "Nine of Clubs", (10,"c"): "Ten of Clubs"
    , (11,"c"): "Jack of Clubs", (12,"c"): "Queen of Clubs", (13,"c"): "King of Clubs",
    
            (1,"s"): "Ace of Spades", (2,"s"): "Two of Spades",(3,"s"):
    "Three of Spades", (4,"s"): "Four of Spades", (5,"s"): "Five of Spades", (6,"s"): "Six of Spades", 
    (7,"s"): "Seven of Spades", (8,"s"): "Eight of Spades", (9,"s"): "Nine of Spades", (10,"s"): "Ten of Spades"
    , (11,"s"): "Jack of Spades", (12,"s"): "Queen of Spades", (13,"s"): "King of Spades"
    }


    def __init__(self, card_list = None):
        if card_list != None:
            self.cards = card_list

            
        else:
            self.cards = [card(key[0], key[1]) for key in deck.deck_of_cards]
            


    
    
    def get_deck(self):
        return self.cards
    
    #does not shuffle. Just resets the deck to the orignal cards
    def reset_deck(self):
        self.cards = [card(key[0], key[1]) for key in deck.deck_of_cards]

    

    
    #returns the key for the top card in the deck
    def draw_card(self):
        if len(self.cards) > 0:
            
            current_card = self.cards[0]
            
            self.cards.pop(0)
            
            return current_card
            
        print("No cards remain in the deck")
        return None
    
    
    def update_deck(self, list_of_cards):
        self.cards = list_of_cards
    
    
    
  
    
    #shuffles the deck randomly
    def shuffle_deck(self):
        #Fisher-Yates Shuffle Algorithm
        for i in range(len(self.cards)):
            #picks a random value ranging from i to the length of the list
            random_index = random.randint(i ,len(self.cards) - 1)
            #swaps the value at index i with the value at random_index
            self.cards[i], self.cards[random_index] = self.cards[random_index], self.cards[i]
    
        
        
        
    #prints the atributes for each card in the deck
    def print_card_keys(self):
        string = "["
        
        for index, current_card in enumerate(self.cards):
            #adds the key to the string
            string += f"{card.get_key(current_card)[0]}{card.get_key(current_card)[1]}"
            
            #adds a comma if it isn't the final card
            if index != len(self.cards) - 1:
                string += ", "
        #finishes the brackets
        string += "]"
        
        print (string)

    
    
    
    #prints all cards
    def __str__(self):
        #string to return
        string = ""
        #loops through the length of the card list
        for index, current_card in enumerate(self.cards):
            #finds the current_key
            current_key = card.get_key(current_card)
            #puts the key into the dictionary
            if index < len(self.cards) - 1:
                string += deck.deck_of_cards[current_key] + ", "
                
            else:
                string += deck.deck_of_cards[current_key]
        
        return string
        


        
    #all cards
    def __repr__(self):
        return self.__str__()
        
        
        
    """
    STATIC METHODS
    """
    
        
    #static method, no instance requirement
    #returns a string for a single card
    #'key' must be a tuple with a length of 2 containing (int, string)
    #int must be in the range 1 - 13
    #string must be either 'h' 'd' 'c' 's'
    def single_card_display (key):
        num = key[0]
        suit = key[1]
        #checks for an invalid key
        if num < 1 or num > 13:
            print(f"Card Print Error (debug: located in Deck __str__) Card value must be greater 0 or less than 14")
            return "NOT VALID"
        
        if suit != "h" and suit != "d" and suit != "c" and suit != "s":
            print(f"Card Print Error (debug: located in Deck __str__) Card suit must be lowercase 'h', 'd', 'c', or 's' ")
            return "NOT VALID"
            
        
        
        #puts key into dictionary
        
        return deck.deck_of_cards[key]
        
        
        
    
    #static method, no instance required
    #sorts cards based on suit, least to greatest
    #input a list of card objects to sort
    #input a list of the suit order. EX. ["h","c","d","s"]
    def sort_cards(card_list, suit_order = ["h","c","d","s"] ):
        
        #list that conains the valid suits
        test = ["h","c","d","s"]
        try:
            #makes sure that the list contains all suits
            if len(suit_order) != 4:
                print("Invalid input for suit_order")
                suit_order = ["h","c","d","s"]
            
            else:
                #checks if the suit is valid and tests for duplicate suits
                for suit in suit_order:
                    
                    if not(suit in test):

                        print("Invalid input for suit_order")
                        return None
                        
                    test.remove(suit)
                    
        except TypeError:
            suit_order = ["h","c","d","s"]
            print("Invalid input for suit_order")
            
            
        
        separated_cards = [[],[],[],[]]
        sorted_cards = []
        
        #loops through the suits
        for index, suit in enumerate(suit_order):
            
            #loops through the card_list and sorts the cards into suit specific lists
            for card_index in range(len(card_list)):
                #trys to call methods involving the current cards
                try:
                    current_card = card_list[card_index]
                    current_suit = card.get_key(current_card)[1]
                    
                except AttributeError:
                    print("list must contain card object")
                    return None
                    
                if current_suit == suit:
                    separated_cards[index].append(current_card)
                
        for index, suit_group in enumerate(separated_cards):
            #uses the .sort function to sort the cards by rank.
            #creates the key that acts as the ace has a rank of 14, and compares every other card normaly. 
            suit_group.sort(key = lambda c:14 if card.get_key(c)[0] == 1 else card.get_key(c)[0])
        
        
        #add all the cards from the group back into one list in order
        for i in range(len(separated_cards)):
            
            current_suit_cards = separated_cards[i]
            
            for j in range(len(current_suit_cards)):
                
                sorted_cards.append(current_suit_cards[j])
        
        
        return sorted_cards
