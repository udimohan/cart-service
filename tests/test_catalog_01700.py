"""Tests for catalog_01700."""

import pytest

from cartservice.generated.catalog_01700 import (
    Product_01700,
    bucket_by_tag_01700,
    is_valid_sku_01700,
    price_with_tax_01700,
)


def test_price_with_tax_01700():
    assert price_with_tax_01700(1000, 500) == 1050


def test_price_with_tax_negative_01700():
    with pytest.raises(ValueError):
        price_with_tax_01700(1000, -1)


def test_is_valid_sku_01700():
    assert is_valid_sku_01700("abc123")
    assert not is_valid_sku_01700("")


def test_bucket_by_tag_01700():
    p = Product_01700("s1", 100, ["a"])
    assert bucket_by_tag_01700([p]) == {"a": ["s1"]}
