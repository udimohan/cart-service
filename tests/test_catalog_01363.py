"""Tests for catalog_01363."""

import pytest

from cartservice.generated.catalog_01363 import (
    Product_01363,
    bucket_by_tag_01363,
    is_valid_sku_01363,
    price_with_tax_01363,
)


def test_price_with_tax_01363():
    assert price_with_tax_01363(1000, 500) == 1050


def test_price_with_tax_negative_01363():
    with pytest.raises(ValueError):
        price_with_tax_01363(1000, -1)


def test_is_valid_sku_01363():
    assert is_valid_sku_01363("abc123")
    assert not is_valid_sku_01363("")


def test_bucket_by_tag_01363():
    p = Product_01363("s1", 100, ["a"])
    assert bucket_by_tag_01363([p]) == {"a": ["s1"]}
