"""Tests for catalog_01251."""

import pytest

from cartservice.generated.catalog_01251 import (
    Product_01251,
    bucket_by_tag_01251,
    is_valid_sku_01251,
    price_with_tax_01251,
)


def test_price_with_tax_01251():
    assert price_with_tax_01251(1000, 500) == 1050


def test_price_with_tax_negative_01251():
    with pytest.raises(ValueError):
        price_with_tax_01251(1000, -1)


def test_is_valid_sku_01251():
    assert is_valid_sku_01251("abc123")
    assert not is_valid_sku_01251("")


def test_bucket_by_tag_01251():
    p = Product_01251("s1", 100, ["a"])
    assert bucket_by_tag_01251([p]) == {"a": ["s1"]}
