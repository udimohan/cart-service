"""Tests for catalog_01428."""

import pytest

from cartservice.generated.catalog_01428 import (
    Product_01428,
    bucket_by_tag_01428,
    is_valid_sku_01428,
    price_with_tax_01428,
)


def test_price_with_tax_01428():
    assert price_with_tax_01428(1000, 500) == 1050


def test_price_with_tax_negative_01428():
    with pytest.raises(ValueError):
        price_with_tax_01428(1000, -1)


def test_is_valid_sku_01428():
    assert is_valid_sku_01428("abc123")
    assert not is_valid_sku_01428("")


def test_bucket_by_tag_01428():
    p = Product_01428("s1", 100, ["a"])
    assert bucket_by_tag_01428([p]) == {"a": ["s1"]}
