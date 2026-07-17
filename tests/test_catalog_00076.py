"""Tests for catalog_00076."""

import pytest

from cartservice.generated.catalog_00076 import (
    Product_00076,
    bucket_by_tag_00076,
    is_valid_sku_00076,
    price_with_tax_00076,
)


def test_price_with_tax_00076():
    assert price_with_tax_00076(1000, 500) == 1050


def test_price_with_tax_negative_00076():
    with pytest.raises(ValueError):
        price_with_tax_00076(1000, -1)


def test_is_valid_sku_00076():
    assert is_valid_sku_00076("abc123")
    assert not is_valid_sku_00076("")


def test_bucket_by_tag_00076():
    p = Product_00076("s1", 100, ["a"])
    assert bucket_by_tag_00076([p]) == {"a": ["s1"]}
