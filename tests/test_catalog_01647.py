"""Tests for catalog_01647."""

import pytest

from cartservice.generated.catalog_01647 import (
    Product_01647,
    bucket_by_tag_01647,
    is_valid_sku_01647,
    price_with_tax_01647,
)


def test_price_with_tax_01647():
    assert price_with_tax_01647(1000, 500) == 1050


def test_price_with_tax_negative_01647():
    with pytest.raises(ValueError):
        price_with_tax_01647(1000, -1)


def test_is_valid_sku_01647():
    assert is_valid_sku_01647("abc123")
    assert not is_valid_sku_01647("")


def test_bucket_by_tag_01647():
    p = Product_01647("s1", 100, ["a"])
    assert bucket_by_tag_01647([p]) == {"a": ["s1"]}
