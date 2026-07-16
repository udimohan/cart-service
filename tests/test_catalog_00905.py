"""Tests for catalog_00905."""

import pytest

from cartservice.generated.catalog_00905 import (
    Product_00905,
    bucket_by_tag_00905,
    is_valid_sku_00905,
    price_with_tax_00905,
)


def test_price_with_tax_00905():
    assert price_with_tax_00905(1000, 500) == 1050


def test_price_with_tax_negative_00905():
    with pytest.raises(ValueError):
        price_with_tax_00905(1000, -1)


def test_is_valid_sku_00905():
    assert is_valid_sku_00905("abc123")
    assert not is_valid_sku_00905("")


def test_bucket_by_tag_00905():
    p = Product_00905("s1", 100, ["a"])
    assert bucket_by_tag_00905([p]) == {"a": ["s1"]}
