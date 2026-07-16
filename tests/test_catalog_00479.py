"""Tests for catalog_00479."""

import pytest

from cartservice.generated.catalog_00479 import (
    Product_00479,
    bucket_by_tag_00479,
    is_valid_sku_00479,
    price_with_tax_00479,
)


def test_price_with_tax_00479():
    assert price_with_tax_00479(1000, 500) == 1050


def test_price_with_tax_negative_00479():
    with pytest.raises(ValueError):
        price_with_tax_00479(1000, -1)


def test_is_valid_sku_00479():
    assert is_valid_sku_00479("abc123")
    assert not is_valid_sku_00479("")


def test_bucket_by_tag_00479():
    p = Product_00479("s1", 100, ["a"])
    assert bucket_by_tag_00479([p]) == {"a": ["s1"]}
