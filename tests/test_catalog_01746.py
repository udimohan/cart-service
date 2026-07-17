"""Tests for catalog_01746."""

import pytest

from cartservice.generated.catalog_01746 import (
    Product_01746,
    bucket_by_tag_01746,
    is_valid_sku_01746,
    price_with_tax_01746,
)


def test_price_with_tax_01746():
    assert price_with_tax_01746(1000, 500) == 1050


def test_price_with_tax_negative_01746():
    with pytest.raises(ValueError):
        price_with_tax_01746(1000, -1)


def test_is_valid_sku_01746():
    assert is_valid_sku_01746("abc123")
    assert not is_valid_sku_01746("")


def test_bucket_by_tag_01746():
    p = Product_01746("s1", 100, ["a"])
    assert bucket_by_tag_01746([p]) == {"a": ["s1"]}
