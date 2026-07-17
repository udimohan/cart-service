"""Tests for catalog_01414."""

import pytest

from cartservice.generated.catalog_01414 import (
    Product_01414,
    bucket_by_tag_01414,
    is_valid_sku_01414,
    price_with_tax_01414,
)


def test_price_with_tax_01414():
    assert price_with_tax_01414(1000, 500) == 1050


def test_price_with_tax_negative_01414():
    with pytest.raises(ValueError):
        price_with_tax_01414(1000, -1)


def test_is_valid_sku_01414():
    assert is_valid_sku_01414("abc123")
    assert not is_valid_sku_01414("")


def test_bucket_by_tag_01414():
    p = Product_01414("s1", 100, ["a"])
    assert bucket_by_tag_01414([p]) == {"a": ["s1"]}
