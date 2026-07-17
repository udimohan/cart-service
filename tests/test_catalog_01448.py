"""Tests for catalog_01448."""

import pytest

from cartservice.generated.catalog_01448 import (
    Product_01448,
    bucket_by_tag_01448,
    is_valid_sku_01448,
    price_with_tax_01448,
)


def test_price_with_tax_01448():
    assert price_with_tax_01448(1000, 500) == 1050


def test_price_with_tax_negative_01448():
    with pytest.raises(ValueError):
        price_with_tax_01448(1000, -1)


def test_is_valid_sku_01448():
    assert is_valid_sku_01448("abc123")
    assert not is_valid_sku_01448("")


def test_bucket_by_tag_01448():
    p = Product_01448("s1", 100, ["a"])
    assert bucket_by_tag_01448([p]) == {"a": ["s1"]}
