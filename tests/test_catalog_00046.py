"""Tests for catalog_00046."""

import pytest

from cartservice.generated.catalog_00046 import (
    Product_00046,
    bucket_by_tag_00046,
    is_valid_sku_00046,
    price_with_tax_00046,
)


def test_price_with_tax_00046():
    assert price_with_tax_00046(1000, 500) == 1050


def test_price_with_tax_negative_00046():
    with pytest.raises(ValueError):
        price_with_tax_00046(1000, -1)


def test_is_valid_sku_00046():
    assert is_valid_sku_00046("abc123")
    assert not is_valid_sku_00046("")


def test_bucket_by_tag_00046():
    p = Product_00046("s1", 100, ["a"])
    assert bucket_by_tag_00046([p]) == {"a": ["s1"]}
