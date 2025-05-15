"""Business-logic for loyalty points."""

from __future__ import annotations

from typing import Dict

CONVERSION_FACTOR: float = 200.0  # AED → 1 point

def calculate_reward(customer_id: str, purchase_amount: float )->float:
    """
    Calculates loyalty points.

    Args:
        customer_id: Customer ID (string or number).
        purchase_amount: Total purchases in AED. Must be ≥ 0.

    Returns:
        Number of points earned (may be fractional).

    Raises:
        ValueError: If the amount or ID is negative.
    """
    if purchase_amount < 0:
        raise ValueError("purchase_amount must be non-negative")

    return purchase_amount / CONVERSION_FACTOR

def generate_coupons(customer_id: str, purchase_amount: float)-> Dict[int, int]:
    if purchase_amount < 0:
        raise ValueError("Purchase amount must be non-negative.")
    
       # Return an empty dict if no points were earned
    return {} if points == 0 else {cid: points}