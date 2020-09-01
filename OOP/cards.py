import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(suit, value) for suit in suits for value in values]
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
            
    
    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")
        return self

    def deal_card(self):
        return self._deal(1)
    
    def deal_hand(self, num):
        return self._deal(num)

d = Deck()
d.shuffle()
d.shuffle()
d.shuffle()
d.shuffle()
print(d.deal_hand(4))