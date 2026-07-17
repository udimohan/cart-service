"""Tests for catalog_00251."""

import pytest

from cartservice.generated.catalog_00251 import (
    Product_00251,
    bucket_by_tag_00251,
    is_valid_sku_00251,
    price_with_tax_00251,
)


def test_price_with_tax_00251():
    assert price_with_tax_00251(1000, 500) == 1050


def test_price_with_tax_negative_00251():
    with pytest.raises(ValueError):
        price_with_tax_00251(1000, -1)


def test_is_valid_sku_00251():
    assert is_valid_sku_00251("abc123")
    assert not is_valid_sku_00251("")


def test_bucket_by_tag_00251():
    p = Product_00251("s1", 100, ["a"])
    assert bucket_by_tag_00251([p]) == {"a": ["s1"]}
