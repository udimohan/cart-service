"""Tests for catalog_01638."""

import pytest

from cartservice.generated.catalog_01638 import (
    Product_01638,
    bucket_by_tag_01638,
    is_valid_sku_01638,
    price_with_tax_01638,
)


def test_price_with_tax_01638():
    assert price_with_tax_01638(1000, 500) == 1050


def test_price_with_tax_negative_01638():
    with pytest.raises(ValueError):
        price_with_tax_01638(1000, -1)


def test_is_valid_sku_01638():
    assert is_valid_sku_01638("abc123")
    assert not is_valid_sku_01638("")


def test_bucket_by_tag_01638():
    p = Product_01638("s1", 100, ["a"])
    assert bucket_by_tag_01638([p]) == {"a": ["s1"]}
