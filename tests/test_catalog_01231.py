"""Tests for catalog_01231."""

import pytest

from cartservice.generated.catalog_01231 import (
    Product_01231,
    bucket_by_tag_01231,
    is_valid_sku_01231,
    price_with_tax_01231,
)


def test_price_with_tax_01231():
    assert price_with_tax_01231(1000, 500) == 1050


def test_price_with_tax_negative_01231():
    with pytest.raises(ValueError):
        price_with_tax_01231(1000, -1)


def test_is_valid_sku_01231():
    assert is_valid_sku_01231("abc123")
    assert not is_valid_sku_01231("")


def test_bucket_by_tag_01231():
    p = Product_01231("s1", 100, ["a"])
    assert bucket_by_tag_01231([p]) == {"a": ["s1"]}
