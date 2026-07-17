"""Tests for catalog_00045."""

import pytest

from cartservice.generated.catalog_00045 import (
    Product_00045,
    bucket_by_tag_00045,
    is_valid_sku_00045,
    price_with_tax_00045,
)


def test_price_with_tax_00045():
    assert price_with_tax_00045(1000, 500) == 1050


def test_price_with_tax_negative_00045():
    with pytest.raises(ValueError):
        price_with_tax_00045(1000, -1)


def test_is_valid_sku_00045():
    assert is_valid_sku_00045("abc123")
    assert not is_valid_sku_00045("")


def test_bucket_by_tag_00045():
    p = Product_00045("s1", 100, ["a"])
    assert bucket_by_tag_00045([p]) == {"a": ["s1"]}
