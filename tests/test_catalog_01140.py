"""Tests for catalog_01140."""

import pytest

from cartservice.generated.catalog_01140 import (
    Product_01140,
    bucket_by_tag_01140,
    is_valid_sku_01140,
    price_with_tax_01140,
)


def test_price_with_tax_01140():
    assert price_with_tax_01140(1000, 500) == 1050


def test_price_with_tax_negative_01140():
    with pytest.raises(ValueError):
        price_with_tax_01140(1000, -1)


def test_is_valid_sku_01140():
    assert is_valid_sku_01140("abc123")
    assert not is_valid_sku_01140("")


def test_bucket_by_tag_01140():
    p = Product_01140("s1", 100, ["a"])
    assert bucket_by_tag_01140([p]) == {"a": ["s1"]}
