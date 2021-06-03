from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

from phrases import *

class Deck:
	def __init__(self, deck_title, colors):
		self.deck_title =  deck_title
		self.colors = colors
		self.text_phrases = []

	def add_convert_phrase(self, phrase):
		add = phrase.replace(" ", ",")
		self.text_phrases.append(add)


def dedup_cards(card_results):
	seen = {}
	cards = []
	for card in card_results:
		if card.name in seen.keys():
			continue
		else:
			seen[card.name] = 1
			cards.append(card)

	print (seen)
	print ([card.name for card in cards])

	return cards


def get_types():
	types = Type.all()
	print (types)

def cards_with_phrases(colors, *phrases):
	search_str = ""
	for phrase in phrases[:-1]:
		search_str += f"{phrase},"

	search_str += phrases[-1]

	cards = Card.where(text=search_str).where(page=1).where(pageSize=20).all()

	for card in dedup_cards(cards):
		print (f"{card.name} ({card.set})")
		print (card.colors)
		print (card.text)
		print ("\n")

def cards_with_converted_phrase(colors, search_str):
	cards = Card.where(colors=colors).where(text=search_str).where(page=1).where(pageSize=10).all()
	for card in dedup_cards(cards):
		print (f"{card.name} ({card.set})")
		print (card.id)
		print (card.printings)
		print (card.colors)
		#print (card.text)
		print ("\n")

def main():
	d = Deck("test_deck", "black|red")
	phrases = [
		"if you control a creature with power 4 or greater"
		]

	[d.add_convert_phrase(phrase) for phrase in phrases]

	for phrase in d.text_phrases:
		cards_with_converted_phrase(d.colors, phrase)

if __name__ == '__main__':
	main()