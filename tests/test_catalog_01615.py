"""Tests for catalog_01615."""

import pytest

from cartservice.generated.catalog_01615 import (
    Product_01615,
    bucket_by_tag_01615,
    is_valid_sku_01615,
    price_with_tax_01615,
)


def test_price_with_tax_01615():
    assert price_with_tax_01615(1000, 500) == 1050


def test_price_with_tax_negative_01615():
    with pytest.raises(ValueError):
        price_with_tax_01615(1000, -1)


def test_is_valid_sku_01615():
    assert is_valid_sku_01615("abc123")
    assert not is_valid_sku_01615("")


def test_bucket_by_tag_01615():
    p = Product_01615("s1", 100, ["a"])
    assert bucket_by_tag_01615([p]) == {"a": ["s1"]}
