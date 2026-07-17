"""Tests for catalog_00113."""

import pytest

from cartservice.generated.catalog_00113 import (
    Product_00113,
    bucket_by_tag_00113,
    is_valid_sku_00113,
    price_with_tax_00113,
)


def test_price_with_tax_00113():
    assert price_with_tax_00113(1000, 500) == 1050


def test_price_with_tax_negative_00113():
    with pytest.raises(ValueError):
        price_with_tax_00113(1000, -1)


def test_is_valid_sku_00113():
    assert is_valid_sku_00113("abc123")
    assert not is_valid_sku_00113("")


def test_bucket_by_tag_00113():
    p = Product_00113("s1", 100, ["a"])
    assert bucket_by_tag_00113([p]) == {"a": ["s1"]}
