"""Tests for catalog_00917."""

import pytest

from cartservice.generated.catalog_00917 import (
    Product_00917,
    bucket_by_tag_00917,
    is_valid_sku_00917,
    price_with_tax_00917,
)


def test_price_with_tax_00917():
    assert price_with_tax_00917(1000, 500) == 1050


def test_price_with_tax_negative_00917():
    with pytest.raises(ValueError):
        price_with_tax_00917(1000, -1)


def test_is_valid_sku_00917():
    assert is_valid_sku_00917("abc123")
    assert not is_valid_sku_00917("")


def test_bucket_by_tag_00917():
    p = Product_00917("s1", 100, ["a"])
    assert bucket_by_tag_00917([p]) == {"a": ["s1"]}
