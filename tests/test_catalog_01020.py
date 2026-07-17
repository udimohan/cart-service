"""Tests for catalog_01020."""

import pytest

from cartservice.generated.catalog_01020 import (
    Product_01020,
    bucket_by_tag_01020,
    is_valid_sku_01020,
    price_with_tax_01020,
)


def test_price_with_tax_01020():
    assert price_with_tax_01020(1000, 500) == 1050


def test_price_with_tax_negative_01020():
    with pytest.raises(ValueError):
        price_with_tax_01020(1000, -1)


def test_is_valid_sku_01020():
    assert is_valid_sku_01020("abc123")
    assert not is_valid_sku_01020("")


def test_bucket_by_tag_01020():
    p = Product_01020("s1", 100, ["a"])
    assert bucket_by_tag_01020([p]) == {"a": ["s1"]}
