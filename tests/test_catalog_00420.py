"""Tests for catalog_00420."""

import pytest

from cartservice.generated.catalog_00420 import (
    Product_00420,
    bucket_by_tag_00420,
    is_valid_sku_00420,
    price_with_tax_00420,
)


def test_price_with_tax_00420():
    assert price_with_tax_00420(1000, 500) == 1050


def test_price_with_tax_negative_00420():
    with pytest.raises(ValueError):
        price_with_tax_00420(1000, -1)


def test_is_valid_sku_00420():
    assert is_valid_sku_00420("abc123")
    assert not is_valid_sku_00420("")


def test_bucket_by_tag_00420():
    p = Product_00420("s1", 100, ["a"])
    assert bucket_by_tag_00420([p]) == {"a": ["s1"]}
