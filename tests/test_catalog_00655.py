"""Tests for catalog_00655."""

import pytest

from cartservice.generated.catalog_00655 import (
    Product_00655,
    bucket_by_tag_00655,
    is_valid_sku_00655,
    price_with_tax_00655,
)


def test_price_with_tax_00655():
    assert price_with_tax_00655(1000, 500) == 1050


def test_price_with_tax_negative_00655():
    with pytest.raises(ValueError):
        price_with_tax_00655(1000, -1)


def test_is_valid_sku_00655():
    assert is_valid_sku_00655("abc123")
    assert not is_valid_sku_00655("")


def test_bucket_by_tag_00655():
    p = Product_00655("s1", 100, ["a"])
    assert bucket_by_tag_00655([p]) == {"a": ["s1"]}
