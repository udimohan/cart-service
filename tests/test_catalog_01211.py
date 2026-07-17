"""Tests for catalog_01211."""

import pytest

from cartservice.generated.catalog_01211 import (
    Product_01211,
    bucket_by_tag_01211,
    is_valid_sku_01211,
    price_with_tax_01211,
)


def test_price_with_tax_01211():
    assert price_with_tax_01211(1000, 500) == 1050


def test_price_with_tax_negative_01211():
    with pytest.raises(ValueError):
        price_with_tax_01211(1000, -1)


def test_is_valid_sku_01211():
    assert is_valid_sku_01211("abc123")
    assert not is_valid_sku_01211("")


def test_bucket_by_tag_01211():
    p = Product_01211("s1", 100, ["a"])
    assert bucket_by_tag_01211([p]) == {"a": ["s1"]}
