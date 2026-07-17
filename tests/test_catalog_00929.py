"""Tests for catalog_00929."""

import pytest

from cartservice.generated.catalog_00929 import (
    Product_00929,
    bucket_by_tag_00929,
    is_valid_sku_00929,
    price_with_tax_00929,
)


def test_price_with_tax_00929():
    assert price_with_tax_00929(1000, 500) == 1050


def test_price_with_tax_negative_00929():
    with pytest.raises(ValueError):
        price_with_tax_00929(1000, -1)


def test_is_valid_sku_00929():
    assert is_valid_sku_00929("abc123")
    assert not is_valid_sku_00929("")


def test_bucket_by_tag_00929():
    p = Product_00929("s1", 100, ["a"])
    assert bucket_by_tag_00929([p]) == {"a": ["s1"]}
