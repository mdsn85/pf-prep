import pytest
from src.loyalty import calculate_reward

def test_reward_for_100_AED():
    points = calculate_reward("member454",100)
    assert points == 0.5

def test_negative_Value_Purchase():
    with pytest.raises(ValueError):
        calculate_reward("cust-1", -20)