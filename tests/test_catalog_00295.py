"""Tests for catalog_00295."""

import pytest

from cartservice.generated.catalog_00295 import (
    Product_00295,
    bucket_by_tag_00295,
    is_valid_sku_00295,
    price_with_tax_00295,
)


def test_price_with_tax_00295():
    assert price_with_tax_00295(1000, 500) == 1050


def test_price_with_tax_negative_00295():
    with pytest.raises(ValueError):
        price_with_tax_00295(1000, -1)


def test_is_valid_sku_00295():
    assert is_valid_sku_00295("abc123")
    assert not is_valid_sku_00295("")


def test_bucket_by_tag_00295():
    p = Product_00295("s1", 100, ["a"])
    assert bucket_by_tag_00295([p]) == {"a": ["s1"]}
