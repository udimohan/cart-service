"""Tests for catalog_01386."""

import pytest

from cartservice.generated.catalog_01386 import (
    Product_01386,
    bucket_by_tag_01386,
    is_valid_sku_01386,
    price_with_tax_01386,
)


def test_price_with_tax_01386():
    assert price_with_tax_01386(1000, 500) == 1050


def test_price_with_tax_negative_01386():
    with pytest.raises(ValueError):
        price_with_tax_01386(1000, -1)


def test_is_valid_sku_01386():
    assert is_valid_sku_01386("abc123")
    assert not is_valid_sku_01386("")


def test_bucket_by_tag_01386():
    p = Product_01386("s1", 100, ["a"])
    assert bucket_by_tag_01386([p]) == {"a": ["s1"]}
