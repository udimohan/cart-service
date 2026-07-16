"""Tests for catalog_01341."""

import pytest

from cartservice.generated.catalog_01341 import (
    Product_01341,
    bucket_by_tag_01341,
    is_valid_sku_01341,
    price_with_tax_01341,
)


def test_price_with_tax_01341():
    assert price_with_tax_01341(1000, 500) == 1050


def test_price_with_tax_negative_01341():
    with pytest.raises(ValueError):
        price_with_tax_01341(1000, -1)


def test_is_valid_sku_01341():
    assert is_valid_sku_01341("abc123")
    assert not is_valid_sku_01341("")


def test_bucket_by_tag_01341():
    p = Product_01341("s1", 100, ["a"])
    assert bucket_by_tag_01341([p]) == {"a": ["s1"]}
