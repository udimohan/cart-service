"""Tests for catalog_00941."""

import pytest

from cartservice.generated.catalog_00941 import (
    Product_00941,
    bucket_by_tag_00941,
    is_valid_sku_00941,
    price_with_tax_00941,
)


def test_price_with_tax_00941():
    assert price_with_tax_00941(1000, 500) == 1050


def test_price_with_tax_negative_00941():
    with pytest.raises(ValueError):
        price_with_tax_00941(1000, -1)


def test_is_valid_sku_00941():
    assert is_valid_sku_00941("abc123")
    assert not is_valid_sku_00941("")


def test_bucket_by_tag_00941():
    p = Product_00941("s1", 100, ["a"])
    assert bucket_by_tag_00941([p]) == {"a": ["s1"]}
