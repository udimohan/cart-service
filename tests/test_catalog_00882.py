"""Tests for catalog_00882."""

import pytest

from cartservice.generated.catalog_00882 import (
    Product_00882,
    bucket_by_tag_00882,
    is_valid_sku_00882,
    price_with_tax_00882,
)


def test_price_with_tax_00882():
    assert price_with_tax_00882(1000, 500) == 1050


def test_price_with_tax_negative_00882():
    with pytest.raises(ValueError):
        price_with_tax_00882(1000, -1)


def test_is_valid_sku_00882():
    assert is_valid_sku_00882("abc123")
    assert not is_valid_sku_00882("")


def test_bucket_by_tag_00882():
    p = Product_00882("s1", 100, ["a"])
    assert bucket_by_tag_00882([p]) == {"a": ["s1"]}
