"""Tests for catalog_00043."""

import pytest

from cartservice.generated.catalog_00043 import (
    Product_00043,
    bucket_by_tag_00043,
    is_valid_sku_00043,
    price_with_tax_00043,
)


def test_price_with_tax_00043():
    assert price_with_tax_00043(1000, 500) == 1050


def test_price_with_tax_negative_00043():
    with pytest.raises(ValueError):
        price_with_tax_00043(1000, -1)


def test_is_valid_sku_00043():
    assert is_valid_sku_00043("abc123")
    assert not is_valid_sku_00043("")


def test_bucket_by_tag_00043():
    p = Product_00043("s1", 100, ["a"])
    assert bucket_by_tag_00043([p]) == {"a": ["s1"]}
