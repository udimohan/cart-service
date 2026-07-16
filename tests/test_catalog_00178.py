"""Tests for catalog_00178."""

import pytest

from cartservice.generated.catalog_00178 import (
    Product_00178,
    bucket_by_tag_00178,
    is_valid_sku_00178,
    price_with_tax_00178,
)


def test_price_with_tax_00178():
    assert price_with_tax_00178(1000, 500) == 1050


def test_price_with_tax_negative_00178():
    with pytest.raises(ValueError):
        price_with_tax_00178(1000, -1)


def test_is_valid_sku_00178():
    assert is_valid_sku_00178("abc123")
    assert not is_valid_sku_00178("")


def test_bucket_by_tag_00178():
    p = Product_00178("s1", 100, ["a"])
    assert bucket_by_tag_00178([p]) == {"a": ["s1"]}
