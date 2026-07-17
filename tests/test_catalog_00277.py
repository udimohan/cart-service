"""Tests for catalog_00277."""

import pytest

from cartservice.generated.catalog_00277 import (
    Product_00277,
    bucket_by_tag_00277,
    is_valid_sku_00277,
    price_with_tax_00277,
)


def test_price_with_tax_00277():
    assert price_with_tax_00277(1000, 500) == 1050


def test_price_with_tax_negative_00277():
    with pytest.raises(ValueError):
        price_with_tax_00277(1000, -1)


def test_is_valid_sku_00277():
    assert is_valid_sku_00277("abc123")
    assert not is_valid_sku_00277("")


def test_bucket_by_tag_00277():
    p = Product_00277("s1", 100, ["a"])
    assert bucket_by_tag_00277([p]) == {"a": ["s1"]}
