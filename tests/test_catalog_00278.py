"""Tests for catalog_00278."""

import pytest

from cartservice.generated.catalog_00278 import (
    Product_00278,
    bucket_by_tag_00278,
    is_valid_sku_00278,
    price_with_tax_00278,
)


def test_price_with_tax_00278():
    assert price_with_tax_00278(1000, 500) == 1050


def test_price_with_tax_negative_00278():
    with pytest.raises(ValueError):
        price_with_tax_00278(1000, -1)


def test_is_valid_sku_00278():
    assert is_valid_sku_00278("abc123")
    assert not is_valid_sku_00278("")


def test_bucket_by_tag_00278():
    p = Product_00278("s1", 100, ["a"])
    assert bucket_by_tag_00278([p]) == {"a": ["s1"]}
