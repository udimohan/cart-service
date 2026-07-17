"""Tests for catalog_01334."""

import pytest

from cartservice.generated.catalog_01334 import (
    Product_01334,
    bucket_by_tag_01334,
    is_valid_sku_01334,
    price_with_tax_01334,
)


def test_price_with_tax_01334():
    assert price_with_tax_01334(1000, 500) == 1050


def test_price_with_tax_negative_01334():
    with pytest.raises(ValueError):
        price_with_tax_01334(1000, -1)


def test_is_valid_sku_01334():
    assert is_valid_sku_01334("abc123")
    assert not is_valid_sku_01334("")


def test_bucket_by_tag_01334():
    p = Product_01334("s1", 100, ["a"])
    assert bucket_by_tag_01334([p]) == {"a": ["s1"]}
