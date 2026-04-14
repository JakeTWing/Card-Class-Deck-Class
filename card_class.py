
class card:
    
    def __init__(self, num, suit):
        self.card_num = num
        self.card_suit = suit
            
    
    #returns card key
    def get_key(self):
        return (self.card_num, self.card_suit)



    #*does not account for suit
    #returns true if two cards have the same rank
    def equal_rank(self, other):
        r1 = self.get_key()[0]
        r2 = other.get_key()[0]    
        
        if r1 == r2:
            return True
        return False
    







    #*takes suit into account
    #returns true if a cards rank and suit matches another cards rank and suit
    def __eq__(self, other):
        r1,s1 = self.get_key()
        r2,s2 = other.get_key()
        
        if r1 == r2 and  s1 == s2:
            return True
        return False
    
    #*ace is considered highest card in calculation
    #returns true if a cards rank is less than another cards rank
    def __lt__(self, other):
        r1 = self.get_key()[0]
        r2 = other.get_key()[0]
        
        if r1 == 1:
            r1 = 14
            
        if r2 == 1:
            r2 = 14
        
        if r1 < r2:
            return True
        return False
    
    #*ace is considered highest card in calculation
    #returns true if a cards rank is greater than another cards rank
    def __gt__(self, other):
        
        r1 = self.get_key()[0]
        r2 = other.get_key()[0]
        
        if r1 == 1:
            r1 = 14
            
        if r2 == 1:
            r2 = 14
        
        if r1 > r2:
            return True
        return False





    #allow printing
    def __str__(self):
        return f"({self.card_num}{self.card_suit})"
    
    def __repr__(self):
        return self.__str__()
