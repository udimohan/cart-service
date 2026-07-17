"""Tests for catalog_00555."""

import pytest

from cartservice.generated.catalog_00555 import (
    Product_00555,
    bucket_by_tag_00555,
    is_valid_sku_00555,
    price_with_tax_00555,
)


def test_price_with_tax_00555():
    assert price_with_tax_00555(1000, 500) == 1050


def test_price_with_tax_negative_00555():
    with pytest.raises(ValueError):
        price_with_tax_00555(1000, -1)


def test_is_valid_sku_00555():
    assert is_valid_sku_00555("abc123")
    assert not is_valid_sku_00555("")


def test_bucket_by_tag_00555():
    p = Product_00555("s1", 100, ["a"])
    assert bucket_by_tag_00555([p]) == {"a": ["s1"]}
