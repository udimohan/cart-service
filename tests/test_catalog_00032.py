"""Tests for catalog_00032."""

import pytest

from cartservice.generated.catalog_00032 import (
    Product_00032,
    bucket_by_tag_00032,
    is_valid_sku_00032,
    price_with_tax_00032,
)


def test_price_with_tax_00032():
    assert price_with_tax_00032(1000, 500) == 1050


def test_price_with_tax_negative_00032():
    with pytest.raises(ValueError):
        price_with_tax_00032(1000, -1)


def test_is_valid_sku_00032():
    assert is_valid_sku_00032("abc123")
    assert not is_valid_sku_00032("")


def test_bucket_by_tag_00032():
    p = Product_00032("s1", 100, ["a"])
    assert bucket_by_tag_00032([p]) == {"a": ["s1"]}
