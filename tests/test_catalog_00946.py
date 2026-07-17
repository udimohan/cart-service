"""Tests for catalog_00946."""

import pytest

from cartservice.generated.catalog_00946 import (
    Product_00946,
    bucket_by_tag_00946,
    is_valid_sku_00946,
    price_with_tax_00946,
)


def test_price_with_tax_00946():
    assert price_with_tax_00946(1000, 500) == 1050


def test_price_with_tax_negative_00946():
    with pytest.raises(ValueError):
        price_with_tax_00946(1000, -1)


def test_is_valid_sku_00946():
    assert is_valid_sku_00946("abc123")
    assert not is_valid_sku_00946("")


def test_bucket_by_tag_00946():
    p = Product_00946("s1", 100, ["a"])
    assert bucket_by_tag_00946([p]) == {"a": ["s1"]}
