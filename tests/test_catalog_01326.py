"""Tests for catalog_01326."""

import pytest

from cartservice.generated.catalog_01326 import (
    Product_01326,
    bucket_by_tag_01326,
    is_valid_sku_01326,
    price_with_tax_01326,
)


def test_price_with_tax_01326():
    assert price_with_tax_01326(1000, 500) == 1050


def test_price_with_tax_negative_01326():
    with pytest.raises(ValueError):
        price_with_tax_01326(1000, -1)


def test_is_valid_sku_01326():
    assert is_valid_sku_01326("abc123")
    assert not is_valid_sku_01326("")


def test_bucket_by_tag_01326():
    p = Product_01326("s1", 100, ["a"])
    assert bucket_by_tag_01326([p]) == {"a": ["s1"]}
