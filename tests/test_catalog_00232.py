"""Tests for catalog_00232."""

import pytest

from cartservice.generated.catalog_00232 import (
    Product_00232,
    bucket_by_tag_00232,
    is_valid_sku_00232,
    price_with_tax_00232,
)


def test_price_with_tax_00232():
    assert price_with_tax_00232(1000, 500) == 1050


def test_price_with_tax_negative_00232():
    with pytest.raises(ValueError):
        price_with_tax_00232(1000, -1)


def test_is_valid_sku_00232():
    assert is_valid_sku_00232("abc123")
    assert not is_valid_sku_00232("")


def test_bucket_by_tag_00232():
    p = Product_00232("s1", 100, ["a"])
    assert bucket_by_tag_00232([p]) == {"a": ["s1"]}
