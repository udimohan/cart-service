"""Tests for catalog_00833."""

import pytest

from cartservice.generated.catalog_00833 import (
    Product_00833,
    bucket_by_tag_00833,
    is_valid_sku_00833,
    price_with_tax_00833,
)


def test_price_with_tax_00833():
    assert price_with_tax_00833(1000, 500) == 1050


def test_price_with_tax_negative_00833():
    with pytest.raises(ValueError):
        price_with_tax_00833(1000, -1)


def test_is_valid_sku_00833():
    assert is_valid_sku_00833("abc123")
    assert not is_valid_sku_00833("")


def test_bucket_by_tag_00833():
    p = Product_00833("s1", 100, ["a"])
    assert bucket_by_tag_00833([p]) == {"a": ["s1"]}
