"""Tests for catalog_00319."""

import pytest

from cartservice.generated.catalog_00319 import (
    Product_00319,
    bucket_by_tag_00319,
    is_valid_sku_00319,
    price_with_tax_00319,
)


def test_price_with_tax_00319():
    assert price_with_tax_00319(1000, 500) == 1050


def test_price_with_tax_negative_00319():
    with pytest.raises(ValueError):
        price_with_tax_00319(1000, -1)


def test_is_valid_sku_00319():
    assert is_valid_sku_00319("abc123")
    assert not is_valid_sku_00319("")


def test_bucket_by_tag_00319():
    p = Product_00319("s1", 100, ["a"])
    assert bucket_by_tag_00319([p]) == {"a": ["s1"]}
