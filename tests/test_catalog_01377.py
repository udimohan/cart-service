"""Tests for catalog_01377."""

import pytest

from cartservice.generated.catalog_01377 import (
    Product_01377,
    bucket_by_tag_01377,
    is_valid_sku_01377,
    price_with_tax_01377,
)


def test_price_with_tax_01377():
    assert price_with_tax_01377(1000, 500) == 1050


def test_price_with_tax_negative_01377():
    with pytest.raises(ValueError):
        price_with_tax_01377(1000, -1)


def test_is_valid_sku_01377():
    assert is_valid_sku_01377("abc123")
    assert not is_valid_sku_01377("")


def test_bucket_by_tag_01377():
    p = Product_01377("s1", 100, ["a"])
    assert bucket_by_tag_01377([p]) == {"a": ["s1"]}
