"""Tests for catalog_00717."""

import pytest

from cartservice.generated.catalog_00717 import (
    Product_00717,
    bucket_by_tag_00717,
    is_valid_sku_00717,
    price_with_tax_00717,
)


def test_price_with_tax_00717():
    assert price_with_tax_00717(1000, 500) == 1050


def test_price_with_tax_negative_00717():
    with pytest.raises(ValueError):
        price_with_tax_00717(1000, -1)


def test_is_valid_sku_00717():
    assert is_valid_sku_00717("abc123")
    assert not is_valid_sku_00717("")


def test_bucket_by_tag_00717():
    p = Product_00717("s1", 100, ["a"])
    assert bucket_by_tag_00717([p]) == {"a": ["s1"]}
