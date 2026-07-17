"""Tests for catalog_01715."""

import pytest

from cartservice.generated.catalog_01715 import (
    Product_01715,
    bucket_by_tag_01715,
    is_valid_sku_01715,
    price_with_tax_01715,
)


def test_price_with_tax_01715():
    assert price_with_tax_01715(1000, 500) == 1050


def test_price_with_tax_negative_01715():
    with pytest.raises(ValueError):
        price_with_tax_01715(1000, -1)


def test_is_valid_sku_01715():
    assert is_valid_sku_01715("abc123")
    assert not is_valid_sku_01715("")


def test_bucket_by_tag_01715():
    p = Product_01715("s1", 100, ["a"])
    assert bucket_by_tag_01715([p]) == {"a": ["s1"]}
