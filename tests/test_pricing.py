"""Tests for cartservice.pricing (some target the intentional bugs)."""

import pytest

from cartservice.pricing import (
    LineItem,
    apply_discount_cents,
    average_price_cents,
    build_receipt,
    line_total_cents,
    subtotal_cents,
)


def test_line_total_basic():
    assert line_total_cents(LineItem("widget", 100, 3)) == 300


def test_subtotal_basic():
    items = [LineItem("a", 100, 2), LineItem("b", 50, 1)]
    assert subtotal_cents(items) == 250


def test_apply_discount_half():
    assert apply_discount_cents(200, 0.5) == 100


def test_negative_quantity_should_be_rejected():
    # BUG #2: currently produces a negative total instead of raising.
    with pytest.raises(ValueError):
        line_total_cents(LineItem("widget", 100, -5))


def test_average_price_full_discount_empty_units():
    # BUG #1: raises ZeroDivisionError today.
    with pytest.raises(ValueError):
        average_price_cents([], 1.0)


def test_build_receipt_no_shared_state():
    # BUG #3: mutable default arg leaks state between calls.
    first = build_receipt(["x"])
    second = build_receipt(["y"])
    assert second["count"] == 1
