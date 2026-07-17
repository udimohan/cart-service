"""Tests for catalog_00398."""

import pytest

from cartservice.generated.catalog_00398 import (
    Product_00398,
    bucket_by_tag_00398,
    is_valid_sku_00398,
    price_with_tax_00398,
)


def test_price_with_tax_00398():
    assert price_with_tax_00398(1000, 500) == 1050


def test_price_with_tax_negative_00398():
    with pytest.raises(ValueError):
        price_with_tax_00398(1000, -1)


def test_is_valid_sku_00398():
    assert is_valid_sku_00398("abc123")
    assert not is_valid_sku_00398("")


def test_bucket_by_tag_00398():
    p = Product_00398("s1", 100, ["a"])
    assert bucket_by_tag_00398([p]) == {"a": ["s1"]}
