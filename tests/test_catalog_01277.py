"""Tests for catalog_01277."""

import pytest

from cartservice.generated.catalog_01277 import (
    Product_01277,
    bucket_by_tag_01277,
    is_valid_sku_01277,
    price_with_tax_01277,
)


def test_price_with_tax_01277():
    assert price_with_tax_01277(1000, 500) == 1050


def test_price_with_tax_negative_01277():
    with pytest.raises(ValueError):
        price_with_tax_01277(1000, -1)


def test_is_valid_sku_01277():
    assert is_valid_sku_01277("abc123")
    assert not is_valid_sku_01277("")


def test_bucket_by_tag_01277():
    p = Product_01277("s1", 100, ["a"])
    assert bucket_by_tag_01277([p]) == {"a": ["s1"]}
