"""Tests for catalog_01255."""

import pytest

from cartservice.generated.catalog_01255 import (
    Product_01255,
    bucket_by_tag_01255,
    is_valid_sku_01255,
    price_with_tax_01255,
)


def test_price_with_tax_01255():
    assert price_with_tax_01255(1000, 500) == 1050


def test_price_with_tax_negative_01255():
    with pytest.raises(ValueError):
        price_with_tax_01255(1000, -1)


def test_is_valid_sku_01255():
    assert is_valid_sku_01255("abc123")
    assert not is_valid_sku_01255("")


def test_bucket_by_tag_01255():
    p = Product_01255("s1", 100, ["a"])
    assert bucket_by_tag_01255([p]) == {"a": ["s1"]}
