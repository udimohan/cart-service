"""Tests for catalog_01048."""

import pytest

from cartservice.generated.catalog_01048 import (
    Product_01048,
    bucket_by_tag_01048,
    is_valid_sku_01048,
    price_with_tax_01048,
)


def test_price_with_tax_01048():
    assert price_with_tax_01048(1000, 500) == 1050


def test_price_with_tax_negative_01048():
    with pytest.raises(ValueError):
        price_with_tax_01048(1000, -1)


def test_is_valid_sku_01048():
    assert is_valid_sku_01048("abc123")
    assert not is_valid_sku_01048("")


def test_bucket_by_tag_01048():
    p = Product_01048("s1", 100, ["a"])
    assert bucket_by_tag_01048([p]) == {"a": ["s1"]}
