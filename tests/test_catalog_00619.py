"""Tests for catalog_00619."""

import pytest

from cartservice.generated.catalog_00619 import (
    Product_00619,
    bucket_by_tag_00619,
    is_valid_sku_00619,
    price_with_tax_00619,
)


def test_price_with_tax_00619():
    assert price_with_tax_00619(1000, 500) == 1050


def test_price_with_tax_negative_00619():
    with pytest.raises(ValueError):
        price_with_tax_00619(1000, -1)


def test_is_valid_sku_00619():
    assert is_valid_sku_00619("abc123")
    assert not is_valid_sku_00619("")


def test_bucket_by_tag_00619():
    p = Product_00619("s1", 100, ["a"])
    assert bucket_by_tag_00619([p]) == {"a": ["s1"]}
