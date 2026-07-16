"""Tests for catalog_01178."""

import pytest

from cartservice.generated.catalog_01178 import (
    Product_01178,
    bucket_by_tag_01178,
    is_valid_sku_01178,
    price_with_tax_01178,
)


def test_price_with_tax_01178():
    assert price_with_tax_01178(1000, 500) == 1050


def test_price_with_tax_negative_01178():
    with pytest.raises(ValueError):
        price_with_tax_01178(1000, -1)


def test_is_valid_sku_01178():
    assert is_valid_sku_01178("abc123")
    assert not is_valid_sku_01178("")


def test_bucket_by_tag_01178():
    p = Product_01178("s1", 100, ["a"])
    assert bucket_by_tag_01178([p]) == {"a": ["s1"]}
