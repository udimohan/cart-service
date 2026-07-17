"""Tests for catalog_01041."""

import pytest

from cartservice.generated.catalog_01041 import (
    Product_01041,
    bucket_by_tag_01041,
    is_valid_sku_01041,
    price_with_tax_01041,
)


def test_price_with_tax_01041():
    assert price_with_tax_01041(1000, 500) == 1050


def test_price_with_tax_negative_01041():
    with pytest.raises(ValueError):
        price_with_tax_01041(1000, -1)


def test_is_valid_sku_01041():
    assert is_valid_sku_01041("abc123")
    assert not is_valid_sku_01041("")


def test_bucket_by_tag_01041():
    p = Product_01041("s1", 100, ["a"])
    assert bucket_by_tag_01041([p]) == {"a": ["s1"]}
