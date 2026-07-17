"""Tests for catalog_00412."""

import pytest

from cartservice.generated.catalog_00412 import (
    Product_00412,
    bucket_by_tag_00412,
    is_valid_sku_00412,
    price_with_tax_00412,
)


def test_price_with_tax_00412():
    assert price_with_tax_00412(1000, 500) == 1050


def test_price_with_tax_negative_00412():
    with pytest.raises(ValueError):
        price_with_tax_00412(1000, -1)


def test_is_valid_sku_00412():
    assert is_valid_sku_00412("abc123")
    assert not is_valid_sku_00412("")


def test_bucket_by_tag_00412():
    p = Product_00412("s1", 100, ["a"])
    assert bucket_by_tag_00412([p]) == {"a": ["s1"]}
