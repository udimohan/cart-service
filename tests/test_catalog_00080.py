"""Tests for catalog_00080."""

import pytest

from cartservice.generated.catalog_00080 import (
    Product_00080,
    bucket_by_tag_00080,
    is_valid_sku_00080,
    price_with_tax_00080,
)


def test_price_with_tax_00080():
    assert price_with_tax_00080(1000, 500) == 1050


def test_price_with_tax_negative_00080():
    with pytest.raises(ValueError):
        price_with_tax_00080(1000, -1)


def test_is_valid_sku_00080():
    assert is_valid_sku_00080("abc123")
    assert not is_valid_sku_00080("")


def test_bucket_by_tag_00080():
    p = Product_00080("s1", 100, ["a"])
    assert bucket_by_tag_00080([p]) == {"a": ["s1"]}
