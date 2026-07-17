"""Tests for catalog_01278."""

import pytest

from cartservice.generated.catalog_01278 import (
    Product_01278,
    bucket_by_tag_01278,
    is_valid_sku_01278,
    price_with_tax_01278,
)


def test_price_with_tax_01278():
    assert price_with_tax_01278(1000, 500) == 1050


def test_price_with_tax_negative_01278():
    with pytest.raises(ValueError):
        price_with_tax_01278(1000, -1)


def test_is_valid_sku_01278():
    assert is_valid_sku_01278("abc123")
    assert not is_valid_sku_01278("")


def test_bucket_by_tag_01278():
    p = Product_01278("s1", 100, ["a"])
    assert bucket_by_tag_01278([p]) == {"a": ["s1"]}
