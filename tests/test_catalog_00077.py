"""Tests for catalog_00077."""

import pytest

from cartservice.generated.catalog_00077 import (
    Product_00077,
    bucket_by_tag_00077,
    is_valid_sku_00077,
    price_with_tax_00077,
)


def test_price_with_tax_00077():
    assert price_with_tax_00077(1000, 500) == 1050


def test_price_with_tax_negative_00077():
    with pytest.raises(ValueError):
        price_with_tax_00077(1000, -1)


def test_is_valid_sku_00077():
    assert is_valid_sku_00077("abc123")
    assert not is_valid_sku_00077("")


def test_bucket_by_tag_00077():
    p = Product_00077("s1", 100, ["a"])
    assert bucket_by_tag_00077([p]) == {"a": ["s1"]}
