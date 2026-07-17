"""Tests for catalog_00332."""

import pytest

from cartservice.generated.catalog_00332 import (
    Product_00332,
    bucket_by_tag_00332,
    is_valid_sku_00332,
    price_with_tax_00332,
)


def test_price_with_tax_00332():
    assert price_with_tax_00332(1000, 500) == 1050


def test_price_with_tax_negative_00332():
    with pytest.raises(ValueError):
        price_with_tax_00332(1000, -1)


def test_is_valid_sku_00332():
    assert is_valid_sku_00332("abc123")
    assert not is_valid_sku_00332("")


def test_bucket_by_tag_00332():
    p = Product_00332("s1", 100, ["a"])
    assert bucket_by_tag_00332([p]) == {"a": ["s1"]}
