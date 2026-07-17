"""Tests for catalog_00063."""

import pytest

from cartservice.generated.catalog_00063 import (
    Product_00063,
    bucket_by_tag_00063,
    is_valid_sku_00063,
    price_with_tax_00063,
)


def test_price_with_tax_00063():
    assert price_with_tax_00063(1000, 500) == 1050


def test_price_with_tax_negative_00063():
    with pytest.raises(ValueError):
        price_with_tax_00063(1000, -1)


def test_is_valid_sku_00063():
    assert is_valid_sku_00063("abc123")
    assert not is_valid_sku_00063("")


def test_bucket_by_tag_00063():
    p = Product_00063("s1", 100, ["a"])
    assert bucket_by_tag_00063([p]) == {"a": ["s1"]}
