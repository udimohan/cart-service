"""Tests for catalog_01669."""

import pytest

from cartservice.generated.catalog_01669 import (
    Product_01669,
    bucket_by_tag_01669,
    is_valid_sku_01669,
    price_with_tax_01669,
)


def test_price_with_tax_01669():
    assert price_with_tax_01669(1000, 500) == 1050


def test_price_with_tax_negative_01669():
    with pytest.raises(ValueError):
        price_with_tax_01669(1000, -1)


def test_is_valid_sku_01669():
    assert is_valid_sku_01669("abc123")
    assert not is_valid_sku_01669("")


def test_bucket_by_tag_01669():
    p = Product_01669("s1", 100, ["a"])
    assert bucket_by_tag_01669([p]) == {"a": ["s1"]}
