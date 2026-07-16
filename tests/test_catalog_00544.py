"""Tests for catalog_00544."""

import pytest

from cartservice.generated.catalog_00544 import (
    Product_00544,
    bucket_by_tag_00544,
    is_valid_sku_00544,
    price_with_tax_00544,
)


def test_price_with_tax_00544():
    assert price_with_tax_00544(1000, 500) == 1050


def test_price_with_tax_negative_00544():
    with pytest.raises(ValueError):
        price_with_tax_00544(1000, -1)


def test_is_valid_sku_00544():
    assert is_valid_sku_00544("abc123")
    assert not is_valid_sku_00544("")


def test_bucket_by_tag_00544():
    p = Product_00544("s1", 100, ["a"])
    assert bucket_by_tag_00544([p]) == {"a": ["s1"]}
