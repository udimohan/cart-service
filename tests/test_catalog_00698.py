"""Tests for catalog_00698."""

import pytest

from cartservice.generated.catalog_00698 import (
    Product_00698,
    bucket_by_tag_00698,
    is_valid_sku_00698,
    price_with_tax_00698,
)


def test_price_with_tax_00698():
    assert price_with_tax_00698(1000, 500) == 1050


def test_price_with_tax_negative_00698():
    with pytest.raises(ValueError):
        price_with_tax_00698(1000, -1)


def test_is_valid_sku_00698():
    assert is_valid_sku_00698("abc123")
    assert not is_valid_sku_00698("")


def test_bucket_by_tag_00698():
    p = Product_00698("s1", 100, ["a"])
    assert bucket_by_tag_00698([p]) == {"a": ["s1"]}
