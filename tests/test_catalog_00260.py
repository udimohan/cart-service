"""Tests for catalog_00260."""

import pytest

from cartservice.generated.catalog_00260 import (
    Product_00260,
    bucket_by_tag_00260,
    is_valid_sku_00260,
    price_with_tax_00260,
)


def test_price_with_tax_00260():
    assert price_with_tax_00260(1000, 500) == 1050


def test_price_with_tax_negative_00260():
    with pytest.raises(ValueError):
        price_with_tax_00260(1000, -1)


def test_is_valid_sku_00260():
    assert is_valid_sku_00260("abc123")
    assert not is_valid_sku_00260("")


def test_bucket_by_tag_00260():
    p = Product_00260("s1", 100, ["a"])
    assert bucket_by_tag_00260([p]) == {"a": ["s1"]}
