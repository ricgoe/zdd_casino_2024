import pytest
from casino.blackjack import count_cards, play_game
from casino.main_classes import CardDeck
from io import StringIO


def test_count_cards():
    assert count_cards(["2", "3", "4"]) == 9

@pytest.mark.parametrize("cards, score", 
                         [(["A", "Q"], 21),
                          (["A", "5", "5"], 21),
                          (["A", "9"], 20),
                          (["A", "A", "7"], 19)
                          ]
                         )
def test_count_cards_with_aces(cards, score):
    assert count_cards(cards) == score

def test_more_than_21():
    assert count_cards(["10", "J", "Q"]) > 21

def test_unknown_cards():
    with pytest.raises(ValueError) as error:
        count_cards(["X"])
    assert "Invalid card: X" in str(error.value)


def test_single_player_blackjack(monkeypatch):
    """Simulate a single player getting Blackjack."""
    def mock_user_input():
        # This simulates the user input
        def fake_input(prompt):
            if "number of players" in prompt:
                return "1"
            return "n"
        return fake_input
    
    def mock_draw_cards(self, n):
        # This simulates the drawing of cards.
        return ["A", "10"]

    # Mock single player game
    monkeypatch.setattr('builtins.input', mock_user_input())

    # Mock CardDeck to deal a Blackjack hand
    monkeypatch.setattr(CardDeck, 'draw_cards', mock_draw_cards)

    # Capture output
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    play_game()

    assert "Player 1, your cards: A, 10" in output.getvalue()
    assert "You have 21 points." in output.getvalue()
    assert "Winner(s): Player 1" in output.getvalue()