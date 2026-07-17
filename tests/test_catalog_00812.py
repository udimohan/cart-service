"""Tests for catalog_00812."""

import pytest

from cartservice.generated.catalog_00812 import (
    Product_00812,
    bucket_by_tag_00812,
    is_valid_sku_00812,
    price_with_tax_00812,
)


def test_price_with_tax_00812():
    assert price_with_tax_00812(1000, 500) == 1050


def test_price_with_tax_negative_00812():
    with pytest.raises(ValueError):
        price_with_tax_00812(1000, -1)


def test_is_valid_sku_00812():
    assert is_valid_sku_00812("abc123")
    assert not is_valid_sku_00812("")


def test_bucket_by_tag_00812():
    p = Product_00812("s1", 100, ["a"])
    assert bucket_by_tag_00812([p]) == {"a": ["s1"]}
