"""Tests for catalog_00371."""

import pytest

from cartservice.generated.catalog_00371 import (
    Product_00371,
    bucket_by_tag_00371,
    is_valid_sku_00371,
    price_with_tax_00371,
)


def test_price_with_tax_00371():
    assert price_with_tax_00371(1000, 500) == 1050


def test_price_with_tax_negative_00371():
    with pytest.raises(ValueError):
        price_with_tax_00371(1000, -1)


def test_is_valid_sku_00371():
    assert is_valid_sku_00371("abc123")
    assert not is_valid_sku_00371("")


def test_bucket_by_tag_00371():
    p = Product_00371("s1", 100, ["a"])
    assert bucket_by_tag_00371([p]) == {"a": ["s1"]}
