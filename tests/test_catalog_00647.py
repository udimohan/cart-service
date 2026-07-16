"""Tests for catalog_00647."""

import pytest

from cartservice.generated.catalog_00647 import (
    Product_00647,
    bucket_by_tag_00647,
    is_valid_sku_00647,
    price_with_tax_00647,
)


def test_price_with_tax_00647():
    assert price_with_tax_00647(1000, 500) == 1050


def test_price_with_tax_negative_00647():
    with pytest.raises(ValueError):
        price_with_tax_00647(1000, -1)


def test_is_valid_sku_00647():
    assert is_valid_sku_00647("abc123")
    assert not is_valid_sku_00647("")


def test_bucket_by_tag_00647():
    p = Product_00647("s1", 100, ["a"])
    assert bucket_by_tag_00647([p]) == {"a": ["s1"]}
