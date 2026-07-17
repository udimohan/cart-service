"""Tests for catalog_01075."""

import pytest

from cartservice.generated.catalog_01075 import (
    Product_01075,
    bucket_by_tag_01075,
    is_valid_sku_01075,
    price_with_tax_01075,
)


def test_price_with_tax_01075():
    assert price_with_tax_01075(1000, 500) == 1050


def test_price_with_tax_negative_01075():
    with pytest.raises(ValueError):
        price_with_tax_01075(1000, -1)


def test_is_valid_sku_01075():
    assert is_valid_sku_01075("abc123")
    assert not is_valid_sku_01075("")


def test_bucket_by_tag_01075():
    p = Product_01075("s1", 100, ["a"])
    assert bucket_by_tag_01075([p]) == {"a": ["s1"]}
