"""Tests for catalog_00271."""

import pytest

from cartservice.generated.catalog_00271 import (
    Product_00271,
    bucket_by_tag_00271,
    is_valid_sku_00271,
    price_with_tax_00271,
)


def test_price_with_tax_00271():
    assert price_with_tax_00271(1000, 500) == 1050


def test_price_with_tax_negative_00271():
    with pytest.raises(ValueError):
        price_with_tax_00271(1000, -1)


def test_is_valid_sku_00271():
    assert is_valid_sku_00271("abc123")
    assert not is_valid_sku_00271("")


def test_bucket_by_tag_00271():
    p = Product_00271("s1", 100, ["a"])
    assert bucket_by_tag_00271([p]) == {"a": ["s1"]}
