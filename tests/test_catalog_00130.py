"""Tests for catalog_00130."""

import pytest

from cartservice.generated.catalog_00130 import (
    Product_00130,
    bucket_by_tag_00130,
    is_valid_sku_00130,
    price_with_tax_00130,
)


def test_price_with_tax_00130():
    assert price_with_tax_00130(1000, 500) == 1050


def test_price_with_tax_negative_00130():
    with pytest.raises(ValueError):
        price_with_tax_00130(1000, -1)


def test_is_valid_sku_00130():
    assert is_valid_sku_00130("abc123")
    assert not is_valid_sku_00130("")


def test_bucket_by_tag_00130():
    p = Product_00130("s1", 100, ["a"])
    assert bucket_by_tag_00130([p]) == {"a": ["s1"]}
