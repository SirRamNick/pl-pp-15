import time

def shuffle_cards(cards, position_even, position_odd):

	for x in range(1, len(cards)+1):

		if x % 2 == 0:
			position_even.append(cards[x-1])
		else:
			position_odd.append(cards[x-1])


def first_step(user_input, position_even, position_odd):

	new_cards_list = []
	if user_input == 'yes':
		for card in position_even:
			new_cards_list.append(card)

		for card in position_odd:
			new_cards_list.append(card)
	elif user_input == 'no':

		for card in position_odd:
			new_cards_list.append(card)

		for card in position_even:
			new_cards_list.append(card)

	return new_cards_list


def second_step(user_input, position_even, position_odd):

	new_cards_list = []

	if user_input == 'yes':
		for card in position_odd:
			new_cards_list.append(card)

		for card in position_even:
			new_cards_list.append(card)

	elif user_input == 'no':
		for card in position_even:
			new_cards_list.append(card)

		for card in position_odd:
			new_cards_list.append(card)

	return new_cards_list


def third_step(user_input, position_even, position_odd):

	new_cards_list = []
	if user_input == 'yes':
		for card in position_even:
			new_cards_list.append(card)

		for card in position_odd:
			new_cards_list.append(card)
	elif user_input == 'no':

		for card in position_odd:
			new_cards_list.append(card)

		for card in position_even:
			new_cards_list.append(card)

	return new_cards_list



def king_or_queen(position_even, position_odd):

	left_cards = []
	right_cards = []

	for card in position_even:
		right_cards.append(card)

	for card in position_odd:
		left_cards.append(card)

	if "King" in right_cards[0]:
		print('Your card is a King')
	else:
		print('Your card is a Queen')

	return left_cards


def color(left_cards):

	_left_cards = []
	right_cards = []

	for x in range(1, len(left_cards)+1):

		if x % 2 == 0:
			_left_cards.append(left_cards[x-1])
		else:
			right_cards.append(left_cards[x-1])

	if "Black" in right_cards[0]:
		print('Your card is color Black')
	else:
		print('Your card is color Red')


	return _left_cards


def suit_of_card(cards_left):

	if "Hearts" in cards_left[1]:
		print('You card is Hearts')

	elif "Spades" in cards_left[1]:
		print('You card is Spades')

	elif "Clubs" in cards_left[1]:
		print('You card is Clubs')

	elif "Diamonds" in cards_left[1]:
		print('You card is Diamonds')