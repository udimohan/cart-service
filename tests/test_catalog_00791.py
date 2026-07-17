"""Tests for catalog_00791."""

import pytest

from cartservice.generated.catalog_00791 import (
    Product_00791,
    bucket_by_tag_00791,
    is_valid_sku_00791,
    price_with_tax_00791,
)


def test_price_with_tax_00791():
    assert price_with_tax_00791(1000, 500) == 1050


def test_price_with_tax_negative_00791():
    with pytest.raises(ValueError):
        price_with_tax_00791(1000, -1)


def test_is_valid_sku_00791():
    assert is_valid_sku_00791("abc123")
    assert not is_valid_sku_00791("")


def test_bucket_by_tag_00791():
    p = Product_00791("s1", 100, ["a"])
    assert bucket_by_tag_00791([p]) == {"a": ["s1"]}
