"""Tests for catalog_01319."""

import pytest

from cartservice.generated.catalog_01319 import (
    Product_01319,
    bucket_by_tag_01319,
    is_valid_sku_01319,
    price_with_tax_01319,
)


def test_price_with_tax_01319():
    assert price_with_tax_01319(1000, 500) == 1050


def test_price_with_tax_negative_01319():
    with pytest.raises(ValueError):
        price_with_tax_01319(1000, -1)


def test_is_valid_sku_01319():
    assert is_valid_sku_01319("abc123")
    assert not is_valid_sku_01319("")


def test_bucket_by_tag_01319():
    p = Product_01319("s1", 100, ["a"])
    assert bucket_by_tag_01319([p]) == {"a": ["s1"]}
