"""Tests for catalog_00142."""

import pytest

from cartservice.generated.catalog_00142 import (
    Product_00142,
    bucket_by_tag_00142,
    is_valid_sku_00142,
    price_with_tax_00142,
)


def test_price_with_tax_00142():
    assert price_with_tax_00142(1000, 500) == 1050


def test_price_with_tax_negative_00142():
    with pytest.raises(ValueError):
        price_with_tax_00142(1000, -1)


def test_is_valid_sku_00142():
    assert is_valid_sku_00142("abc123")
    assert not is_valid_sku_00142("")


def test_bucket_by_tag_00142():
    p = Product_00142("s1", 100, ["a"])
    assert bucket_by_tag_00142([p]) == {"a": ["s1"]}
