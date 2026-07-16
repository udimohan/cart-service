"""Tests for catalog_00347."""

import pytest

from cartservice.generated.catalog_00347 import (
    Product_00347,
    bucket_by_tag_00347,
    is_valid_sku_00347,
    price_with_tax_00347,
)


def test_price_with_tax_00347():
    assert price_with_tax_00347(1000, 500) == 1050


def test_price_with_tax_negative_00347():
    with pytest.raises(ValueError):
        price_with_tax_00347(1000, -1)


def test_is_valid_sku_00347():
    assert is_valid_sku_00347("abc123")
    assert not is_valid_sku_00347("")


def test_bucket_by_tag_00347():
    p = Product_00347("s1", 100, ["a"])
    assert bucket_by_tag_00347([p]) == {"a": ["s1"]}
