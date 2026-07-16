"""Tests for catalog_00106."""

import pytest

from cartservice.generated.catalog_00106 import (
    Product_00106,
    bucket_by_tag_00106,
    is_valid_sku_00106,
    price_with_tax_00106,
)


def test_price_with_tax_00106():
    assert price_with_tax_00106(1000, 500) == 1050


def test_price_with_tax_negative_00106():
    with pytest.raises(ValueError):
        price_with_tax_00106(1000, -1)


def test_is_valid_sku_00106():
    assert is_valid_sku_00106("abc123")
    assert not is_valid_sku_00106("")


def test_bucket_by_tag_00106():
    p = Product_00106("s1", 100, ["a"])
    assert bucket_by_tag_00106([p]) == {"a": ["s1"]}
