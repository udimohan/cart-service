"""Tests for catalog_00312."""

import pytest

from cartservice.generated.catalog_00312 import (
    Product_00312,
    bucket_by_tag_00312,
    is_valid_sku_00312,
    price_with_tax_00312,
)


def test_price_with_tax_00312():
    assert price_with_tax_00312(1000, 500) == 1050


def test_price_with_tax_negative_00312():
    with pytest.raises(ValueError):
        price_with_tax_00312(1000, -1)


def test_is_valid_sku_00312():
    assert is_valid_sku_00312("abc123")
    assert not is_valid_sku_00312("")


def test_bucket_by_tag_00312():
    p = Product_00312("s1", 100, ["a"])
    assert bucket_by_tag_00312([p]) == {"a": ["s1"]}
