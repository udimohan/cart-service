"""Tests for catalog_00943."""

import pytest

from cartservice.generated.catalog_00943 import (
    Product_00943,
    bucket_by_tag_00943,
    is_valid_sku_00943,
    price_with_tax_00943,
)


def test_price_with_tax_00943():
    assert price_with_tax_00943(1000, 500) == 1050


def test_price_with_tax_negative_00943():
    with pytest.raises(ValueError):
        price_with_tax_00943(1000, -1)


def test_is_valid_sku_00943():
    assert is_valid_sku_00943("abc123")
    assert not is_valid_sku_00943("")


def test_bucket_by_tag_00943():
    p = Product_00943("s1", 100, ["a"])
    assert bucket_by_tag_00943([p]) == {"a": ["s1"]}
