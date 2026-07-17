"""Tests for catalog_01737."""

import pytest

from cartservice.generated.catalog_01737 import (
    Product_01737,
    bucket_by_tag_01737,
    is_valid_sku_01737,
    price_with_tax_01737,
)


def test_price_with_tax_01737():
    assert price_with_tax_01737(1000, 500) == 1050


def test_price_with_tax_negative_01737():
    with pytest.raises(ValueError):
        price_with_tax_01737(1000, -1)


def test_is_valid_sku_01737():
    assert is_valid_sku_01737("abc123")
    assert not is_valid_sku_01737("")


def test_bucket_by_tag_01737():
    p = Product_01737("s1", 100, ["a"])
    assert bucket_by_tag_01737([p]) == {"a": ["s1"]}
