"""Tests for catalog_00762."""

import pytest

from cartservice.generated.catalog_00762 import (
    Product_00762,
    bucket_by_tag_00762,
    is_valid_sku_00762,
    price_with_tax_00762,
)


def test_price_with_tax_00762():
    assert price_with_tax_00762(1000, 500) == 1050


def test_price_with_tax_negative_00762():
    with pytest.raises(ValueError):
        price_with_tax_00762(1000, -1)


def test_is_valid_sku_00762():
    assert is_valid_sku_00762("abc123")
    assert not is_valid_sku_00762("")


def test_bucket_by_tag_00762():
    p = Product_00762("s1", 100, ["a"])
    assert bucket_by_tag_00762([p]) == {"a": ["s1"]}
