"""Tests for catalog_00128."""

import pytest

from cartservice.generated.catalog_00128 import (
    Product_00128,
    bucket_by_tag_00128,
    is_valid_sku_00128,
    price_with_tax_00128,
)


def test_price_with_tax_00128():
    assert price_with_tax_00128(1000, 500) == 1050


def test_price_with_tax_negative_00128():
    with pytest.raises(ValueError):
        price_with_tax_00128(1000, -1)


def test_is_valid_sku_00128():
    assert is_valid_sku_00128("abc123")
    assert not is_valid_sku_00128("")


def test_bucket_by_tag_00128():
    p = Product_00128("s1", 100, ["a"])
    assert bucket_by_tag_00128([p]) == {"a": ["s1"]}
