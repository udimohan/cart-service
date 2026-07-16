"""Tests for catalog_01238."""

import pytest

from cartservice.generated.catalog_01238 import (
    Product_01238,
    bucket_by_tag_01238,
    is_valid_sku_01238,
    price_with_tax_01238,
)


def test_price_with_tax_01238():
    assert price_with_tax_01238(1000, 500) == 1050


def test_price_with_tax_negative_01238():
    with pytest.raises(ValueError):
        price_with_tax_01238(1000, -1)


def test_is_valid_sku_01238():
    assert is_valid_sku_01238("abc123")
    assert not is_valid_sku_01238("")


def test_bucket_by_tag_01238():
    p = Product_01238("s1", 100, ["a"])
    assert bucket_by_tag_01238([p]) == {"a": ["s1"]}
