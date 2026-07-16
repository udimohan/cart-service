"""Tests for catalog_01149."""

import pytest

from cartservice.generated.catalog_01149 import (
    Product_01149,
    bucket_by_tag_01149,
    is_valid_sku_01149,
    price_with_tax_01149,
)


def test_price_with_tax_01149():
    assert price_with_tax_01149(1000, 500) == 1050


def test_price_with_tax_negative_01149():
    with pytest.raises(ValueError):
        price_with_tax_01149(1000, -1)


def test_is_valid_sku_01149():
    assert is_valid_sku_01149("abc123")
    assert not is_valid_sku_01149("")


def test_bucket_by_tag_01149():
    p = Product_01149("s1", 100, ["a"])
    assert bucket_by_tag_01149([p]) == {"a": ["s1"]}
