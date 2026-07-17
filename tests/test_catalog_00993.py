"""Tests for catalog_00993."""

import pytest

from cartservice.generated.catalog_00993 import (
    Product_00993,
    bucket_by_tag_00993,
    is_valid_sku_00993,
    price_with_tax_00993,
)


def test_price_with_tax_00993():
    assert price_with_tax_00993(1000, 500) == 1050


def test_price_with_tax_negative_00993():
    with pytest.raises(ValueError):
        price_with_tax_00993(1000, -1)


def test_is_valid_sku_00993():
    assert is_valid_sku_00993("abc123")
    assert not is_valid_sku_00993("")


def test_bucket_by_tag_00993():
    p = Product_00993("s1", 100, ["a"])
    assert bucket_by_tag_00993([p]) == {"a": ["s1"]}
