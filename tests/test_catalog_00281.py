"""Tests for catalog_00281."""

import pytest

from cartservice.generated.catalog_00281 import (
    Product_00281,
    bucket_by_tag_00281,
    is_valid_sku_00281,
    price_with_tax_00281,
)


def test_price_with_tax_00281():
    assert price_with_tax_00281(1000, 500) == 1050


def test_price_with_tax_negative_00281():
    with pytest.raises(ValueError):
        price_with_tax_00281(1000, -1)


def test_is_valid_sku_00281():
    assert is_valid_sku_00281("abc123")
    assert not is_valid_sku_00281("")


def test_bucket_by_tag_00281():
    p = Product_00281("s1", 100, ["a"])
    assert bucket_by_tag_00281([p]) == {"a": ["s1"]}
