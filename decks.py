class Deck:
	def __init__(self, deck_title, colors, deck_format):
		self.deck_title =  deck_title
		self.colors = colors
		self.text_phrases = []

		if deck_format in ["standard", "future", "historic", "gladiator", "pioneer", "modern", "legacy", "pauper", "vintage", "penny", "commander", "brawl", "duel", "oldschool"]:
			self.deck_format = deck_format

		else:
			self.deck_format = "standard"

def br_sacrifice_deck():
	phrases = [
		"you sacrifice",
		"whenever you sacrifice",
		"sacrifice a creature",
		"from your graveyard",
		"learn"
	]

	deck = Deck("BR Sacrifice", ["b","r"], "standard")
	deck.text_phrases = phrases

	return deck