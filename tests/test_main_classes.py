from casino.main_classes import CardDeck

def test_card_deck():
    deck = CardDeck()
    assert len(deck.cards) == 52

def test_draw_cards():
    deck = CardDeck(num_copies=1)
    card = deck.draw_cards(1)
    assert card not in deck.cards
    assert card == ["A"]
