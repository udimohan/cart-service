"""Tests for catalog_00162."""

import pytest

from cartservice.generated.catalog_00162 import (
    Product_00162,
    bucket_by_tag_00162,
    is_valid_sku_00162,
    price_with_tax_00162,
)


def test_price_with_tax_00162():
    assert price_with_tax_00162(1000, 500) == 1050


def test_price_with_tax_negative_00162():
    with pytest.raises(ValueError):
        price_with_tax_00162(1000, -1)


def test_is_valid_sku_00162():
    assert is_valid_sku_00162("abc123")
    assert not is_valid_sku_00162("")


def test_bucket_by_tag_00162():
    p = Product_00162("s1", 100, ["a"])
    assert bucket_by_tag_00162([p]) == {"a": ["s1"]}
