"""Tests for catalog_01292."""

import pytest

from cartservice.generated.catalog_01292 import (
    Product_01292,
    bucket_by_tag_01292,
    is_valid_sku_01292,
    price_with_tax_01292,
)


def test_price_with_tax_01292():
    assert price_with_tax_01292(1000, 500) == 1050


def test_price_with_tax_negative_01292():
    with pytest.raises(ValueError):
        price_with_tax_01292(1000, -1)


def test_is_valid_sku_01292():
    assert is_valid_sku_01292("abc123")
    assert not is_valid_sku_01292("")


def test_bucket_by_tag_01292():
    p = Product_01292("s1", 100, ["a"])
    assert bucket_by_tag_01292([p]) == {"a": ["s1"]}
