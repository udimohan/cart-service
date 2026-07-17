"""Tests for catalog_00380."""

import pytest

from cartservice.generated.catalog_00380 import (
    Product_00380,
    bucket_by_tag_00380,
    is_valid_sku_00380,
    price_with_tax_00380,
)


def test_price_with_tax_00380():
    assert price_with_tax_00380(1000, 500) == 1050


def test_price_with_tax_negative_00380():
    with pytest.raises(ValueError):
        price_with_tax_00380(1000, -1)


def test_is_valid_sku_00380():
    assert is_valid_sku_00380("abc123")
    assert not is_valid_sku_00380("")


def test_bucket_by_tag_00380():
    p = Product_00380("s1", 100, ["a"])
    assert bucket_by_tag_00380([p]) == {"a": ["s1"]}
