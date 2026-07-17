"""Tests for catalog_00783."""

import pytest

from cartservice.generated.catalog_00783 import (
    Product_00783,
    bucket_by_tag_00783,
    is_valid_sku_00783,
    price_with_tax_00783,
)


def test_price_with_tax_00783():
    assert price_with_tax_00783(1000, 500) == 1050


def test_price_with_tax_negative_00783():
    with pytest.raises(ValueError):
        price_with_tax_00783(1000, -1)


def test_is_valid_sku_00783():
    assert is_valid_sku_00783("abc123")
    assert not is_valid_sku_00783("")


def test_bucket_by_tag_00783():
    p = Product_00783("s1", 100, ["a"])
    assert bucket_by_tag_00783([p]) == {"a": ["s1"]}
