"""Tests for catalog_01113."""

import pytest

from cartservice.generated.catalog_01113 import (
    Product_01113,
    bucket_by_tag_01113,
    is_valid_sku_01113,
    price_with_tax_01113,
)


def test_price_with_tax_01113():
    assert price_with_tax_01113(1000, 500) == 1050


def test_price_with_tax_negative_01113():
    with pytest.raises(ValueError):
        price_with_tax_01113(1000, -1)


def test_is_valid_sku_01113():
    assert is_valid_sku_01113("abc123")
    assert not is_valid_sku_01113("")


def test_bucket_by_tag_01113():
    p = Product_01113("s1", 100, ["a"])
    assert bucket_by_tag_01113([p]) == {"a": ["s1"]}
