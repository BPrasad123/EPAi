# EPAI Session 6

## vals
It contains the values of cards for each suit. In total there are 13 cards in a suit starting from 2 to Ace. Jack, queen, king and ace are resprented as 11, 12, 13 and 14 respectively.
## suits
There are four different groups of cards in a pack such as hearts, diamonds, clubs and spades. Each group is called as a suit with 13 cards each. 
## deck_first
It is a combination of all the values from vals and suits. The total number of combinations is equal to 52 that is the total number of cards in a pack. It is result of a function created with lambda, map and zip.
## create_deck
It is a function without the usage of lambda, map and zip. It is another way of creating a deck.
## get_hands_and_winner
It is the main function of the program that creates two hands based on the number of cards specified. It also calls subsequent programs to decide the winner.
## card_split
It simply takes a hand and returns two lists: one with the values of all the cards in hans and another with the suits for all the cards in the hand.
## royal_flush
royal flush (plural royal flushes) (poker) Ace-high straight flush; a hand consisting of the cards A, K, Q, J, 10, of the same suit. This is the rarest and strongest hand in poker. The function returns true if the condition is satisfied.
## straight_flush
All cards in a sequence, all in the same suit.. The function returns true if the condition is satisfied.
## four_of_a_kind
Four-of-a-Kind is second on the list of standard poker hand rankings and consists of four cards of the same rank.
## full_house
A Full House is any three cards of the same number or face value, plus any other two cards of the same number or face value. The function returns true if the condition is satisfied.
## flush
All cards of the same suit, but not in a sequence. The function returns true if the condition is satisfied.
## straight
All cards in a sequence, but not of the same suit. The function returns true if the condition is satisfied.
## three_of_a_kind
Three cards of the same rank. The function returns true if the condition is satisfied.
## two_pair
Two different pairs in a hand. The function returns true if the condition is satisfied.
## one_pair
One pair in a hand. The function returns true if the condition is satisfied.
## high_card
When none of the above ranks is achieved then the highest card is considered for comparison.
## get_highest_rank
It takes a hand and tries to find out the higest ranks depending upon the number of cards in it.
## decide_winner
This function takes two hands and finds out which one is the winner
## test_manual_20_combinations
It takes hardcoded 20 pairs of hands and asserts the winner so as to ensure the entire set of functions are working fine.
## test_more_than_5_cards
This function raises value error if there is an input with more than 5 cards in hand.
## test_less_than_three_cards
This function raises value error if there is an input with less than 3 cards in hand.

## test_two_pair
This fucntion takes a hand as input and tries to find if two paris of cards each of same rank is present in it.
## test_full_house3
This fucntion takes a hand as input and tries to find if full house is satisfied with three cards in the hand.
## test_full_house4
This fucntion takes a hand as input and tries to find if full house is satisfied with four cards in the hand.

## test_royal_flush3
This fucntion takes a hand as input and tries to find if full house is satisfied with three cards in the hand.
## test_royal_flush4
This fucntion takes a hand as input and tries to find if full house is satisfied with four cards in the hand.

## test_one_pair
it takes a hand as input and tries to find if one pair of cards of same ranks is present.
## test_three_of_a_kind
it takes a hand as input and tries to find if three cards of same ranks is present.

## test_straight1
it takes a hand as input and tries to find if all cards in a sequence, but not of the same suit

## test_straight2
it takes a hand as input and tries to find if all cards in a sequence, but not of the same suit with ace included close to 2
## test_straight3
it takes a hand as input and tries to find if all cards in a sequence, but not of the same suit with ace included close to king
## test_flush
It takes a hand as input and tries to find if all cards of the same suit, but not in a sequence
## test_straight_flush1
it takes a hand as input and tries to find if All cards in a sequence, all in the same suit.

## test_straight_flush2
it takes a hand as input and tries to find if All cards in a sequence, all in the same suit with ace included close to 2

## test_straight_flush3
it takes a hand as input and tries to find if All cards in a sequence, all in the same suit with ace included close to king

## test_card_split
It takes a hand and slits the values and suits and validates that both the lists contain same number of elements.