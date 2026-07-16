"""Tests for catalog_00405."""

import pytest

from cartservice.generated.catalog_00405 import (
    Product_00405,
    bucket_by_tag_00405,
    is_valid_sku_00405,
    price_with_tax_00405,
)


def test_price_with_tax_00405():
    assert price_with_tax_00405(1000, 500) == 1050


def test_price_with_tax_negative_00405():
    with pytest.raises(ValueError):
        price_with_tax_00405(1000, -1)


def test_is_valid_sku_00405():
    assert is_valid_sku_00405("abc123")
    assert not is_valid_sku_00405("")


def test_bucket_by_tag_00405():
    p = Product_00405("s1", 100, ["a"])
    assert bucket_by_tag_00405([p]) == {"a": ["s1"]}
