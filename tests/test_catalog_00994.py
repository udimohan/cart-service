"""Tests for catalog_00994."""

import pytest

from cartservice.generated.catalog_00994 import (
    Product_00994,
    bucket_by_tag_00994,
    is_valid_sku_00994,
    price_with_tax_00994,
)


def test_price_with_tax_00994():
    assert price_with_tax_00994(1000, 500) == 1050


def test_price_with_tax_negative_00994():
    with pytest.raises(ValueError):
        price_with_tax_00994(1000, -1)


def test_is_valid_sku_00994():
    assert is_valid_sku_00994("abc123")
    assert not is_valid_sku_00994("")


def test_bucket_by_tag_00994():
    p = Product_00994("s1", 100, ["a"])
    assert bucket_by_tag_00994([p]) == {"a": ["s1"]}
