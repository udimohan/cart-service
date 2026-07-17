"""Tests for catalog_00257."""

import pytest

from cartservice.generated.catalog_00257 import (
    Product_00257,
    bucket_by_tag_00257,
    is_valid_sku_00257,
    price_with_tax_00257,
)


def test_price_with_tax_00257():
    assert price_with_tax_00257(1000, 500) == 1050


def test_price_with_tax_negative_00257():
    with pytest.raises(ValueError):
        price_with_tax_00257(1000, -1)


def test_is_valid_sku_00257():
    assert is_valid_sku_00257("abc123")
    assert not is_valid_sku_00257("")


def test_bucket_by_tag_00257():
    p = Product_00257("s1", 100, ["a"])
    assert bucket_by_tag_00257([p]) == {"a": ["s1"]}
