import pytest
from casino.blackjack import count_cards


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
