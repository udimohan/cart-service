"""Tests for catalog_00231."""

import pytest

from cartservice.generated.catalog_00231 import (
    Product_00231,
    bucket_by_tag_00231,
    is_valid_sku_00231,
    price_with_tax_00231,
)


def test_price_with_tax_00231():
    assert price_with_tax_00231(1000, 500) == 1050


def test_price_with_tax_negative_00231():
    with pytest.raises(ValueError):
        price_with_tax_00231(1000, -1)


def test_is_valid_sku_00231():
    assert is_valid_sku_00231("abc123")
    assert not is_valid_sku_00231("")


def test_bucket_by_tag_00231():
    p = Product_00231("s1", 100, ["a"])
    assert bucket_by_tag_00231([p]) == {"a": ["s1"]}
