"""Tests for catalog_00963."""

import pytest

from cartservice.generated.catalog_00963 import (
    Product_00963,
    bucket_by_tag_00963,
    is_valid_sku_00963,
    price_with_tax_00963,
)


def test_price_with_tax_00963():
    assert price_with_tax_00963(1000, 500) == 1050


def test_price_with_tax_negative_00963():
    with pytest.raises(ValueError):
        price_with_tax_00963(1000, -1)


def test_is_valid_sku_00963():
    assert is_valid_sku_00963("abc123")
    assert not is_valid_sku_00963("")


def test_bucket_by_tag_00963():
    p = Product_00963("s1", 100, ["a"])
    assert bucket_by_tag_00963([p]) == {"a": ["s1"]}
