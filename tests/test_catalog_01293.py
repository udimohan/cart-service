"""Tests for catalog_01293."""

import pytest

from cartservice.generated.catalog_01293 import (
    Product_01293,
    bucket_by_tag_01293,
    is_valid_sku_01293,
    price_with_tax_01293,
)


def test_price_with_tax_01293():
    assert price_with_tax_01293(1000, 500) == 1050


def test_price_with_tax_negative_01293():
    with pytest.raises(ValueError):
        price_with_tax_01293(1000, -1)


def test_is_valid_sku_01293():
    assert is_valid_sku_01293("abc123")
    assert not is_valid_sku_01293("")


def test_bucket_by_tag_01293():
    p = Product_01293("s1", 100, ["a"])
    assert bucket_by_tag_01293([p]) == {"a": ["s1"]}
