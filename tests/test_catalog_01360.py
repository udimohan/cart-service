"""Tests for catalog_01360."""

import pytest

from cartservice.generated.catalog_01360 import (
    Product_01360,
    bucket_by_tag_01360,
    is_valid_sku_01360,
    price_with_tax_01360,
)


def test_price_with_tax_01360():
    assert price_with_tax_01360(1000, 500) == 1050


def test_price_with_tax_negative_01360():
    with pytest.raises(ValueError):
        price_with_tax_01360(1000, -1)


def test_is_valid_sku_01360():
    assert is_valid_sku_01360("abc123")
    assert not is_valid_sku_01360("")


def test_bucket_by_tag_01360():
    p = Product_01360("s1", 100, ["a"])
    assert bucket_by_tag_01360([p]) == {"a": ["s1"]}
