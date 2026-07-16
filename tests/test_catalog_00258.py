"""Tests for catalog_00258."""

import pytest

from cartservice.generated.catalog_00258 import (
    Product_00258,
    bucket_by_tag_00258,
    is_valid_sku_00258,
    price_with_tax_00258,
)


def test_price_with_tax_00258():
    assert price_with_tax_00258(1000, 500) == 1050


def test_price_with_tax_negative_00258():
    with pytest.raises(ValueError):
        price_with_tax_00258(1000, -1)


def test_is_valid_sku_00258():
    assert is_valid_sku_00258("abc123")
    assert not is_valid_sku_00258("")


def test_bucket_by_tag_00258():
    p = Product_00258("s1", 100, ["a"])
    assert bucket_by_tag_00258([p]) == {"a": ["s1"]}
