"""Tests for catalog_01379."""

import pytest

from cartservice.generated.catalog_01379 import (
    Product_01379,
    bucket_by_tag_01379,
    is_valid_sku_01379,
    price_with_tax_01379,
)


def test_price_with_tax_01379():
    assert price_with_tax_01379(1000, 500) == 1050


def test_price_with_tax_negative_01379():
    with pytest.raises(ValueError):
        price_with_tax_01379(1000, -1)


def test_is_valid_sku_01379():
    assert is_valid_sku_01379("abc123")
    assert not is_valid_sku_01379("")


def test_bucket_by_tag_01379():
    p = Product_01379("s1", 100, ["a"])
    assert bucket_by_tag_01379([p]) == {"a": ["s1"]}
