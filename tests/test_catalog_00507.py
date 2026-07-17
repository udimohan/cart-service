"""Tests for catalog_00507."""

import pytest

from cartservice.generated.catalog_00507 import (
    Product_00507,
    bucket_by_tag_00507,
    is_valid_sku_00507,
    price_with_tax_00507,
)


def test_price_with_tax_00507():
    assert price_with_tax_00507(1000, 500) == 1050


def test_price_with_tax_negative_00507():
    with pytest.raises(ValueError):
        price_with_tax_00507(1000, -1)


def test_is_valid_sku_00507():
    assert is_valid_sku_00507("abc123")
    assert not is_valid_sku_00507("")


def test_bucket_by_tag_00507():
    p = Product_00507("s1", 100, ["a"])
    assert bucket_by_tag_00507([p]) == {"a": ["s1"]}
