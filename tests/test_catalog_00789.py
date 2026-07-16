"""Tests for catalog_00789."""

import pytest

from cartservice.generated.catalog_00789 import (
    Product_00789,
    bucket_by_tag_00789,
    is_valid_sku_00789,
    price_with_tax_00789,
)


def test_price_with_tax_00789():
    assert price_with_tax_00789(1000, 500) == 1050


def test_price_with_tax_negative_00789():
    with pytest.raises(ValueError):
        price_with_tax_00789(1000, -1)


def test_is_valid_sku_00789():
    assert is_valid_sku_00789("abc123")
    assert not is_valid_sku_00789("")


def test_bucket_by_tag_00789():
    p = Product_00789("s1", 100, ["a"])
    assert bucket_by_tag_00789([p]) == {"a": ["s1"]}
