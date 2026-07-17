"""Tests for catalog_01185."""

import pytest

from cartservice.generated.catalog_01185 import (
    Product_01185,
    bucket_by_tag_01185,
    is_valid_sku_01185,
    price_with_tax_01185,
)


def test_price_with_tax_01185():
    assert price_with_tax_01185(1000, 500) == 1050


def test_price_with_tax_negative_01185():
    with pytest.raises(ValueError):
        price_with_tax_01185(1000, -1)


def test_is_valid_sku_01185():
    assert is_valid_sku_01185("abc123")
    assert not is_valid_sku_01185("")


def test_bucket_by_tag_01185():
    p = Product_01185("s1", 100, ["a"])
    assert bucket_by_tag_01185([p]) == {"a": ["s1"]}
