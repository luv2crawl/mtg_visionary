import requests
from requests.utils import requote_uri
from pprint import pprint
import os
import json
from decks import *

def get_card_by_name(name):
	url = "https://api.scryfall.com/cards/named?exact="
	url += requote_uri(f'{name}')
	r = requests.get(url)
	j = r.json()

def excluded_colors(selected_colors):
	#return colors not in the list of colors selected for our deck
	color_list = ["w", "u", "r", "b", "g"]
	return list(set(color_list) - set(selected_colors)) + list(set(selected_colors) - set(color_list))

def get_cards_by_keywords(colors, keyphrase, deck_format="standard"):
	url = "https://api.scryfall.com/cards/search?order=cmc&q="
	color_str = f"(c:{' or c:'.join(colors)})"
	exclude = f"-c:{' -c:'.join(excluded_colors(colors))}"

	url += requote_uri(f'{color_str} {exclude} o:"{keyphrase}" f:{deck_format}')

	r = requests.get(url)
	j = r.json()
	
	print (f"[+] {len(j['data'])} results found for phrase: '{keyphrase}' [+]\n\n")

	num_results = j['total_cards']

	results = []

	for card in j['data']:
		if card.get('card_faces', None):
			#handle cards that are more than one card
			for card_face in card['card_faces']:
				results.append(parse_card(card_face))
		else:
			#handle normal cards
			results.append(parse_card(card))

	[pprint(i) for i in results[:2]]


def parse_card(card):
	out = {
		'name': card.get('name', None),
		'rarity': card.get('rarity', None),
		'set_name': f"{card.get('set_name', None)} ({card.get('set', None)})",
		'scryfall_url': card.get('scryfall_uri', None),
		'colors': card.get('colors', None),
		'mana_cost': card.get('mana_cost', None),
		'cmc': card.get('cmc', None),
		'type': card.get('type_line', None),
		'power': card.get('power', None),
		'toughness': card.get('toughness', None),
		'keywords': card.get('keywords', None),
		'text': card.get('oracle_text', None),
		'related_links': card.get('related_uris', None)
	}

	return json.dumps(out)
	

def parse_multi_card(multicard):

	for card in multicard['card_faces']:
		out = {
			'name': card.get('name', None),
			'rarity': card.get('rarity', None),
			'set_name': f"{card.get('set_name', None)} ({card.get('set', None)})",
			'scryfall_url': card.get('scryfall_uri', None),
			'colors': card.get('colors', None),
			'mana_cost': card.get('mana_cost', None),
			'cmc': card.get('cmc', None),
			'type': card.get('type_line', None),
			'power': card.get('power', None),
			'toughness': card.get('toughness', None),
			'keywords': card.get('keywords', None),
			'text': card.get('oracle_text', None),
			'related_links': card.get('related_uris', None)
		}




def main():
	sacdeck = br_sacrifice_deck()
	for phrase in sacdeck.text_phrases:
		get_cards_by_keywords(sacdeck.colors, phrase, sacdeck.deck_format)
	
	#get_card_by_name("Egon, God of Death")

if __name__ == '__main__':
	main()