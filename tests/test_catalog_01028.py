"""Tests for catalog_01028."""

import pytest

from cartservice.generated.catalog_01028 import (
    Product_01028,
    bucket_by_tag_01028,
    is_valid_sku_01028,
    price_with_tax_01028,
)


def test_price_with_tax_01028():
    assert price_with_tax_01028(1000, 500) == 1050


def test_price_with_tax_negative_01028():
    with pytest.raises(ValueError):
        price_with_tax_01028(1000, -1)


def test_is_valid_sku_01028():
    assert is_valid_sku_01028("abc123")
    assert not is_valid_sku_01028("")


def test_bucket_by_tag_01028():
    p = Product_01028("s1", 100, ["a"])
    assert bucket_by_tag_01028([p]) == {"a": ["s1"]}
