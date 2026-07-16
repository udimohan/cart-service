"""Tests for catalog_00116."""

import pytest

from cartservice.generated.catalog_00116 import (
    Product_00116,
    bucket_by_tag_00116,
    is_valid_sku_00116,
    price_with_tax_00116,
)


def test_price_with_tax_00116():
    assert price_with_tax_00116(1000, 500) == 1050


def test_price_with_tax_negative_00116():
    with pytest.raises(ValueError):
        price_with_tax_00116(1000, -1)


def test_is_valid_sku_00116():
    assert is_valid_sku_00116("abc123")
    assert not is_valid_sku_00116("")


def test_bucket_by_tag_00116():
    p = Product_00116("s1", 100, ["a"])
    assert bucket_by_tag_00116([p]) == {"a": ["s1"]}
