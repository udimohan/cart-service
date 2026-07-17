"""Tests for catalog_01523."""

import pytest

from cartservice.generated.catalog_01523 import (
    Product_01523,
    bucket_by_tag_01523,
    is_valid_sku_01523,
    price_with_tax_01523,
)


def test_price_with_tax_01523():
    assert price_with_tax_01523(1000, 500) == 1050


def test_price_with_tax_negative_01523():
    with pytest.raises(ValueError):
        price_with_tax_01523(1000, -1)


def test_is_valid_sku_01523():
    assert is_valid_sku_01523("abc123")
    assert not is_valid_sku_01523("")


def test_bucket_by_tag_01523():
    p = Product_01523("s1", 100, ["a"])
    assert bucket_by_tag_01523([p]) == {"a": ["s1"]}
