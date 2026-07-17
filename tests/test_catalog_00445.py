"""Tests for catalog_00445."""

import pytest

from cartservice.generated.catalog_00445 import (
    Product_00445,
    bucket_by_tag_00445,
    is_valid_sku_00445,
    price_with_tax_00445,
)


def test_price_with_tax_00445():
    assert price_with_tax_00445(1000, 500) == 1050


def test_price_with_tax_negative_00445():
    with pytest.raises(ValueError):
        price_with_tax_00445(1000, -1)


def test_is_valid_sku_00445():
    assert is_valid_sku_00445("abc123")
    assert not is_valid_sku_00445("")


def test_bucket_by_tag_00445():
    p = Product_00445("s1", 100, ["a"])
    assert bucket_by_tag_00445([p]) == {"a": ["s1"]}
