"""Tests for catalog_00661."""

import pytest

from cartservice.generated.catalog_00661 import (
    Product_00661,
    bucket_by_tag_00661,
    is_valid_sku_00661,
    price_with_tax_00661,
)


def test_price_with_tax_00661():
    assert price_with_tax_00661(1000, 500) == 1050


def test_price_with_tax_negative_00661():
    with pytest.raises(ValueError):
        price_with_tax_00661(1000, -1)


def test_is_valid_sku_00661():
    assert is_valid_sku_00661("abc123")
    assert not is_valid_sku_00661("")


def test_bucket_by_tag_00661():
    p = Product_00661("s1", 100, ["a"])
    assert bucket_by_tag_00661([p]) == {"a": ["s1"]}
