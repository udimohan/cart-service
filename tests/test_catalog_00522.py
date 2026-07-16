"""Tests for catalog_00522."""

import pytest

from cartservice.generated.catalog_00522 import (
    Product_00522,
    bucket_by_tag_00522,
    is_valid_sku_00522,
    price_with_tax_00522,
)


def test_price_with_tax_00522():
    assert price_with_tax_00522(1000, 500) == 1050


def test_price_with_tax_negative_00522():
    with pytest.raises(ValueError):
        price_with_tax_00522(1000, -1)


def test_is_valid_sku_00522():
    assert is_valid_sku_00522("abc123")
    assert not is_valid_sku_00522("")


def test_bucket_by_tag_00522():
    p = Product_00522("s1", 100, ["a"])
    assert bucket_by_tag_00522([p]) == {"a": ["s1"]}
