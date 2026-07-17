"""Tests for catalog_00846."""

import pytest

from cartservice.generated.catalog_00846 import (
    Product_00846,
    bucket_by_tag_00846,
    is_valid_sku_00846,
    price_with_tax_00846,
)


def test_price_with_tax_00846():
    assert price_with_tax_00846(1000, 500) == 1050


def test_price_with_tax_negative_00846():
    with pytest.raises(ValueError):
        price_with_tax_00846(1000, -1)


def test_is_valid_sku_00846():
    assert is_valid_sku_00846("abc123")
    assert not is_valid_sku_00846("")


def test_bucket_by_tag_00846():
    p = Product_00846("s1", 100, ["a"])
    assert bucket_by_tag_00846([p]) == {"a": ["s1"]}
