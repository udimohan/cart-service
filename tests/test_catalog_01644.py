"""Tests for catalog_01644."""

import pytest

from cartservice.generated.catalog_01644 import (
    Product_01644,
    bucket_by_tag_01644,
    is_valid_sku_01644,
    price_with_tax_01644,
)


def test_price_with_tax_01644():
    assert price_with_tax_01644(1000, 500) == 1050


def test_price_with_tax_negative_01644():
    with pytest.raises(ValueError):
        price_with_tax_01644(1000, -1)


def test_is_valid_sku_01644():
    assert is_valid_sku_01644("abc123")
    assert not is_valid_sku_01644("")


def test_bucket_by_tag_01644():
    p = Product_01644("s1", 100, ["a"])
    assert bucket_by_tag_01644([p]) == {"a": ["s1"]}
