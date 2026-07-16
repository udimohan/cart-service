"""Tests for catalog_01712."""

import pytest

from cartservice.generated.catalog_01712 import (
    Product_01712,
    bucket_by_tag_01712,
    is_valid_sku_01712,
    price_with_tax_01712,
)


def test_price_with_tax_01712():
    assert price_with_tax_01712(1000, 500) == 1050


def test_price_with_tax_negative_01712():
    with pytest.raises(ValueError):
        price_with_tax_01712(1000, -1)


def test_is_valid_sku_01712():
    assert is_valid_sku_01712("abc123")
    assert not is_valid_sku_01712("")


def test_bucket_by_tag_01712():
    p = Product_01712("s1", 100, ["a"])
    assert bucket_by_tag_01712([p]) == {"a": ["s1"]}
