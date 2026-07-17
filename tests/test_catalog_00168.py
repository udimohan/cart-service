"""Tests for catalog_00168."""

import pytest

from cartservice.generated.catalog_00168 import (
    Product_00168,
    bucket_by_tag_00168,
    is_valid_sku_00168,
    price_with_tax_00168,
)


def test_price_with_tax_00168():
    assert price_with_tax_00168(1000, 500) == 1050


def test_price_with_tax_negative_00168():
    with pytest.raises(ValueError):
        price_with_tax_00168(1000, -1)


def test_is_valid_sku_00168():
    assert is_valid_sku_00168("abc123")
    assert not is_valid_sku_00168("")


def test_bucket_by_tag_00168():
    p = Product_00168("s1", 100, ["a"])
    assert bucket_by_tag_00168([p]) == {"a": ["s1"]}
