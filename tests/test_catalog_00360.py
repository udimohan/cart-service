"""Tests for catalog_00360."""

import pytest

from cartservice.generated.catalog_00360 import (
    Product_00360,
    bucket_by_tag_00360,
    is_valid_sku_00360,
    price_with_tax_00360,
)


def test_price_with_tax_00360():
    assert price_with_tax_00360(1000, 500) == 1050


def test_price_with_tax_negative_00360():
    with pytest.raises(ValueError):
        price_with_tax_00360(1000, -1)


def test_is_valid_sku_00360():
    assert is_valid_sku_00360("abc123")
    assert not is_valid_sku_00360("")


def test_bucket_by_tag_00360():
    p = Product_00360("s1", 100, ["a"])
    assert bucket_by_tag_00360([p]) == {"a": ["s1"]}
