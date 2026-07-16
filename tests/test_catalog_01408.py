"""Tests for catalog_01408."""

import pytest

from cartservice.generated.catalog_01408 import (
    Product_01408,
    bucket_by_tag_01408,
    is_valid_sku_01408,
    price_with_tax_01408,
)


def test_price_with_tax_01408():
    assert price_with_tax_01408(1000, 500) == 1050


def test_price_with_tax_negative_01408():
    with pytest.raises(ValueError):
        price_with_tax_01408(1000, -1)


def test_is_valid_sku_01408():
    assert is_valid_sku_01408("abc123")
    assert not is_valid_sku_01408("")


def test_bucket_by_tag_01408():
    p = Product_01408("s1", 100, ["a"])
    assert bucket_by_tag_01408([p]) == {"a": ["s1"]}
