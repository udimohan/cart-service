"""Tests for catalog_00988."""

import pytest

from cartservice.generated.catalog_00988 import (
    Product_00988,
    bucket_by_tag_00988,
    is_valid_sku_00988,
    price_with_tax_00988,
)


def test_price_with_tax_00988():
    assert price_with_tax_00988(1000, 500) == 1050


def test_price_with_tax_negative_00988():
    with pytest.raises(ValueError):
        price_with_tax_00988(1000, -1)


def test_is_valid_sku_00988():
    assert is_valid_sku_00988("abc123")
    assert not is_valid_sku_00988("")


def test_bucket_by_tag_00988():
    p = Product_00988("s1", 100, ["a"])
    assert bucket_by_tag_00988([p]) == {"a": ["s1"]}
