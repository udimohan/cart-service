"""Tests for catalog_01384."""

import pytest

from cartservice.generated.catalog_01384 import (
    Product_01384,
    bucket_by_tag_01384,
    is_valid_sku_01384,
    price_with_tax_01384,
)


def test_price_with_tax_01384():
    assert price_with_tax_01384(1000, 500) == 1050


def test_price_with_tax_negative_01384():
    with pytest.raises(ValueError):
        price_with_tax_01384(1000, -1)


def test_is_valid_sku_01384():
    assert is_valid_sku_01384("abc123")
    assert not is_valid_sku_01384("")


def test_bucket_by_tag_01384():
    p = Product_01384("s1", 100, ["a"])
    assert bucket_by_tag_01384([p]) == {"a": ["s1"]}
