"""Tests for catalog_01604."""

import pytest

from cartservice.generated.catalog_01604 import (
    Product_01604,
    bucket_by_tag_01604,
    is_valid_sku_01604,
    price_with_tax_01604,
)


def test_price_with_tax_01604():
    assert price_with_tax_01604(1000, 500) == 1050


def test_price_with_tax_negative_01604():
    with pytest.raises(ValueError):
        price_with_tax_01604(1000, -1)


def test_is_valid_sku_01604():
    assert is_valid_sku_01604("abc123")
    assert not is_valid_sku_01604("")


def test_bucket_by_tag_01604():
    p = Product_01604("s1", 100, ["a"])
    assert bucket_by_tag_01604([p]) == {"a": ["s1"]}
