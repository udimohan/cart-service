"""Tests for catalog_00427."""

import pytest

from cartservice.generated.catalog_00427 import (
    Product_00427,
    bucket_by_tag_00427,
    is_valid_sku_00427,
    price_with_tax_00427,
)


def test_price_with_tax_00427():
    assert price_with_tax_00427(1000, 500) == 1050


def test_price_with_tax_negative_00427():
    with pytest.raises(ValueError):
        price_with_tax_00427(1000, -1)


def test_is_valid_sku_00427():
    assert is_valid_sku_00427("abc123")
    assert not is_valid_sku_00427("")


def test_bucket_by_tag_00427():
    p = Product_00427("s1", 100, ["a"])
    assert bucket_by_tag_00427([p]) == {"a": ["s1"]}
