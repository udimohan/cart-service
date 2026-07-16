"""Tests for catalog_01475."""

import pytest

from cartservice.generated.catalog_01475 import (
    Product_01475,
    bucket_by_tag_01475,
    is_valid_sku_01475,
    price_with_tax_01475,
)


def test_price_with_tax_01475():
    assert price_with_tax_01475(1000, 500) == 1050


def test_price_with_tax_negative_01475():
    with pytest.raises(ValueError):
        price_with_tax_01475(1000, -1)


def test_is_valid_sku_01475():
    assert is_valid_sku_01475("abc123")
    assert not is_valid_sku_01475("")


def test_bucket_by_tag_01475():
    p = Product_01475("s1", 100, ["a"])
    assert bucket_by_tag_01475([p]) == {"a": ["s1"]}
