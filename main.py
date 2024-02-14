from card_functions import first_step, second_step, third_step, king_or_queen, color, shuffle_cards, suit_of_card
import time


cards_list = ["King of Clubs (Black)", "King of Hearts (Red)", "King of Spades (Black)", "King of Diamonds (Red)",
			"Queen of Clubs (Black)", "Queen of Hearts (Red)", "Queen of Spades (Black)", "Queen of Diamonds (Red)",]

position_even = []
position_odd = []


if __name__ == '__main__':

	shuffle_cards(cards_list, position_even, position_odd)

	print(position_even)
	user_input = input("Do you see your card here?: ")

	cards_list = first_step(user_input, position_even, position_odd)
	position_even = []
	position_odd = []
	shuffle_cards(cards_list, position_even, position_odd)

	print(position_even)
	user_input = input("Do you see your card here?: ")

	cards_list = second_step(user_input, position_even, position_odd)
	position_even = []
	position_odd = []
	shuffle_cards(cards_list, position_even, position_odd)

	print(position_even)
	user_input = input("Do you see your card here?: ")

	cards_list = third_step(user_input, position_even, position_odd)
	position_even = []
	position_odd = []
	shuffle_cards(cards_list, position_even, position_odd)

	time.sleep(5)
	left_cards = king_or_queen(position_even, position_odd)
	time.sleep(5)
	cards_left = color(left_cards)
	time.sleep(5)
	suit_of_card(cards_left)
	time.sleep(3)

	print(f'Your card is {cards_left[0]}')