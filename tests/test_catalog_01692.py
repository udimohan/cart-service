"""Tests for catalog_01692."""

import pytest

from cartservice.generated.catalog_01692 import (
    Product_01692,
    bucket_by_tag_01692,
    is_valid_sku_01692,
    price_with_tax_01692,
)


def test_price_with_tax_01692():
    assert price_with_tax_01692(1000, 500) == 1050


def test_price_with_tax_negative_01692():
    with pytest.raises(ValueError):
        price_with_tax_01692(1000, -1)


def test_is_valid_sku_01692():
    assert is_valid_sku_01692("abc123")
    assert not is_valid_sku_01692("")


def test_bucket_by_tag_01692():
    p = Product_01692("s1", 100, ["a"])
    assert bucket_by_tag_01692([p]) == {"a": ["s1"]}
