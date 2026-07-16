"""Tests for catalog_00920."""

import pytest

from cartservice.generated.catalog_00920 import (
    Product_00920,
    bucket_by_tag_00920,
    is_valid_sku_00920,
    price_with_tax_00920,
)


def test_price_with_tax_00920():
    assert price_with_tax_00920(1000, 500) == 1050


def test_price_with_tax_negative_00920():
    with pytest.raises(ValueError):
        price_with_tax_00920(1000, -1)


def test_is_valid_sku_00920():
    assert is_valid_sku_00920("abc123")
    assert not is_valid_sku_00920("")


def test_bucket_by_tag_00920():
    p = Product_00920("s1", 100, ["a"])
    assert bucket_by_tag_00920([p]) == {"a": ["s1"]}
