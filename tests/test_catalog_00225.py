"""Tests for catalog_00225."""

import pytest

from cartservice.generated.catalog_00225 import (
    Product_00225,
    bucket_by_tag_00225,
    is_valid_sku_00225,
    price_with_tax_00225,
)


def test_price_with_tax_00225():
    assert price_with_tax_00225(1000, 500) == 1050


def test_price_with_tax_negative_00225():
    with pytest.raises(ValueError):
        price_with_tax_00225(1000, -1)


def test_is_valid_sku_00225():
    assert is_valid_sku_00225("abc123")
    assert not is_valid_sku_00225("")


def test_bucket_by_tag_00225():
    p = Product_00225("s1", 100, ["a"])
    assert bucket_by_tag_00225([p]) == {"a": ["s1"]}
