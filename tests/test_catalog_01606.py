"""Tests for catalog_01606."""

import pytest

from cartservice.generated.catalog_01606 import (
    Product_01606,
    bucket_by_tag_01606,
    is_valid_sku_01606,
    price_with_tax_01606,
)


def test_price_with_tax_01606():
    assert price_with_tax_01606(1000, 500) == 1050


def test_price_with_tax_negative_01606():
    with pytest.raises(ValueError):
        price_with_tax_01606(1000, -1)


def test_is_valid_sku_01606():
    assert is_valid_sku_01606("abc123")
    assert not is_valid_sku_01606("")


def test_bucket_by_tag_01606():
    p = Product_01606("s1", 100, ["a"])
    assert bucket_by_tag_01606([p]) == {"a": ["s1"]}
