"""Tests for catalog_00836."""

import pytest

from cartservice.generated.catalog_00836 import (
    Product_00836,
    bucket_by_tag_00836,
    is_valid_sku_00836,
    price_with_tax_00836,
)


def test_price_with_tax_00836():
    assert price_with_tax_00836(1000, 500) == 1050


def test_price_with_tax_negative_00836():
    with pytest.raises(ValueError):
        price_with_tax_00836(1000, -1)


def test_is_valid_sku_00836():
    assert is_valid_sku_00836("abc123")
    assert not is_valid_sku_00836("")


def test_bucket_by_tag_00836():
    p = Product_00836("s1", 100, ["a"])
    assert bucket_by_tag_00836([p]) == {"a": ["s1"]}
