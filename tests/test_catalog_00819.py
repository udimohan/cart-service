"""Tests for catalog_00819."""

import pytest

from cartservice.generated.catalog_00819 import (
    Product_00819,
    bucket_by_tag_00819,
    is_valid_sku_00819,
    price_with_tax_00819,
)


def test_price_with_tax_00819():
    assert price_with_tax_00819(1000, 500) == 1050


def test_price_with_tax_negative_00819():
    with pytest.raises(ValueError):
        price_with_tax_00819(1000, -1)


def test_is_valid_sku_00819():
    assert is_valid_sku_00819("abc123")
    assert not is_valid_sku_00819("")


def test_bucket_by_tag_00819():
    p = Product_00819("s1", 100, ["a"])
    assert bucket_by_tag_00819([p]) == {"a": ["s1"]}
