"""Tests for catalog_00158."""

import pytest

from cartservice.generated.catalog_00158 import (
    Product_00158,
    bucket_by_tag_00158,
    is_valid_sku_00158,
    price_with_tax_00158,
)


def test_price_with_tax_00158():
    assert price_with_tax_00158(1000, 500) == 1050


def test_price_with_tax_negative_00158():
    with pytest.raises(ValueError):
        price_with_tax_00158(1000, -1)


def test_is_valid_sku_00158():
    assert is_valid_sku_00158("abc123")
    assert not is_valid_sku_00158("")


def test_bucket_by_tag_00158():
    p = Product_00158("s1", 100, ["a"])
    assert bucket_by_tag_00158([p]) == {"a": ["s1"]}
