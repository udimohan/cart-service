"""Tests for catalog_01133."""

import pytest

from cartservice.generated.catalog_01133 import (
    Product_01133,
    bucket_by_tag_01133,
    is_valid_sku_01133,
    price_with_tax_01133,
)


def test_price_with_tax_01133():
    assert price_with_tax_01133(1000, 500) == 1050


def test_price_with_tax_negative_01133():
    with pytest.raises(ValueError):
        price_with_tax_01133(1000, -1)


def test_is_valid_sku_01133():
    assert is_valid_sku_01133("abc123")
    assert not is_valid_sku_01133("")


def test_bucket_by_tag_01133():
    p = Product_01133("s1", 100, ["a"])
    assert bucket_by_tag_01133([p]) == {"a": ["s1"]}
