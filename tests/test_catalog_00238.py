"""Tests for catalog_00238."""

import pytest

from cartservice.generated.catalog_00238 import (
    Product_00238,
    bucket_by_tag_00238,
    is_valid_sku_00238,
    price_with_tax_00238,
)


def test_price_with_tax_00238():
    assert price_with_tax_00238(1000, 500) == 1050


def test_price_with_tax_negative_00238():
    with pytest.raises(ValueError):
        price_with_tax_00238(1000, -1)


def test_is_valid_sku_00238():
    assert is_valid_sku_00238("abc123")
    assert not is_valid_sku_00238("")


def test_bucket_by_tag_00238():
    p = Product_00238("s1", 100, ["a"])
    assert bucket_by_tag_00238([p]) == {"a": ["s1"]}
