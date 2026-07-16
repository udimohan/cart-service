"""Tests for catalog_00028."""

import pytest

from cartservice.generated.catalog_00028 import (
    Product_00028,
    bucket_by_tag_00028,
    is_valid_sku_00028,
    price_with_tax_00028,
)


def test_price_with_tax_00028():
    assert price_with_tax_00028(1000, 500) == 1050


def test_price_with_tax_negative_00028():
    with pytest.raises(ValueError):
        price_with_tax_00028(1000, -1)


def test_is_valid_sku_00028():
    assert is_valid_sku_00028("abc123")
    assert not is_valid_sku_00028("")


def test_bucket_by_tag_00028():
    p = Product_00028("s1", 100, ["a"])
    assert bucket_by_tag_00028([p]) == {"a": ["s1"]}
