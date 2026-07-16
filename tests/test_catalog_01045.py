"""Tests for catalog_01045."""

import pytest

from cartservice.generated.catalog_01045 import (
    Product_01045,
    bucket_by_tag_01045,
    is_valid_sku_01045,
    price_with_tax_01045,
)


def test_price_with_tax_01045():
    assert price_with_tax_01045(1000, 500) == 1050


def test_price_with_tax_negative_01045():
    with pytest.raises(ValueError):
        price_with_tax_01045(1000, -1)


def test_is_valid_sku_01045():
    assert is_valid_sku_01045("abc123")
    assert not is_valid_sku_01045("")


def test_bucket_by_tag_01045():
    p = Product_01045("s1", 100, ["a"])
    assert bucket_by_tag_01045([p]) == {"a": ["s1"]}
