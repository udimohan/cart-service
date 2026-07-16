"""Tests for catalog_00203."""

import pytest

from cartservice.generated.catalog_00203 import (
    Product_00203,
    bucket_by_tag_00203,
    is_valid_sku_00203,
    price_with_tax_00203,
)


def test_price_with_tax_00203():
    assert price_with_tax_00203(1000, 500) == 1050


def test_price_with_tax_negative_00203():
    with pytest.raises(ValueError):
        price_with_tax_00203(1000, -1)


def test_is_valid_sku_00203():
    assert is_valid_sku_00203("abc123")
    assert not is_valid_sku_00203("")


def test_bucket_by_tag_00203():
    p = Product_00203("s1", 100, ["a"])
    assert bucket_by_tag_00203([p]) == {"a": ["s1"]}
