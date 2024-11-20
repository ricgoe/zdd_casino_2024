from casino.main_classes import CardDeck


def count_cards(cards):
    """Calculates the total value of the given cards in a blackjack game.

    Face cards (J, Q, K) count as 10, numbered cards count as their value,
    and Aces count as 11 or 1, adjusting to avoid going over 21.

    Args:
        cards (list of str): A list of card values, e.g., ['A', '7', 'K'].
	"""
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    total = 0
    aces = 0
    for card in cards:
        if card not in card_values:
            raise ValueError(f"Invalid card: {card}")

        # Add card value to total
        total += card_values[card]
        if card == 'A':
            aces += 1

    # Adjust for Aces if total is over 21
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def play_game():
    """A game of Blackjack with multiple players."""
    num_players = int(input("Enter the number of players: "))
    players = [{'name': f"Player {i+1}", 'cards': [], 'score': 0} for i in range(num_players)]

    card_deck = CardDeck(num_copies=4)
    card_deck.shuffle()

    # Initial dealing of two cards
    for player in players:
        player['cards'] = card_deck.draw_cards(2)

    # Each player's turn
    for player in players:
        while True:
            print(f"{player['name']}, your cards: {', '.join(player['cards'])}")
            player['score'] = count_cards(player['cards'])
            print(f"You have {player['score']} points.")

            if player['score'] >= 21:
                break

            answer = input("Do you want another card? (y/n): ")
            if answer.lower() == 'n':
                break

            player['cards'] += card_deck.draw_cards(1)

    # Determine winner
    winning_score = max(player['score'] for player in players if player['score'] <= 21)
    winners = [player['name'] for player in players if player['score'] == winning_score]

    # Final scores and winner announcement
    print("\nFinal Scores:")
    for player in players:
        print(f"{player['name']}: {player['score']} points")
    
    if winners:
        print(f"Winner(s): {', '.join(winners)}")
    else:
        print("No winners this round.")

if __name__ == "__main__":
    play_game()
