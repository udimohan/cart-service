"""Tests for catalog_00484."""

import pytest

from cartservice.generated.catalog_00484 import (
    Product_00484,
    bucket_by_tag_00484,
    is_valid_sku_00484,
    price_with_tax_00484,
)


def test_price_with_tax_00484():
    assert price_with_tax_00484(1000, 500) == 1050


def test_price_with_tax_negative_00484():
    with pytest.raises(ValueError):
        price_with_tax_00484(1000, -1)


def test_is_valid_sku_00484():
    assert is_valid_sku_00484("abc123")
    assert not is_valid_sku_00484("")


def test_bucket_by_tag_00484():
    p = Product_00484("s1", 100, ["a"])
    assert bucket_by_tag_00484([p]) == {"a": ["s1"]}
