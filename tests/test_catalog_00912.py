"""Tests for catalog_00912."""

import pytest

from cartservice.generated.catalog_00912 import (
    Product_00912,
    bucket_by_tag_00912,
    is_valid_sku_00912,
    price_with_tax_00912,
)


def test_price_with_tax_00912():
    assert price_with_tax_00912(1000, 500) == 1050


def test_price_with_tax_negative_00912():
    with pytest.raises(ValueError):
        price_with_tax_00912(1000, -1)


def test_is_valid_sku_00912():
    assert is_valid_sku_00912("abc123")
    assert not is_valid_sku_00912("")


def test_bucket_by_tag_00912():
    p = Product_00912("s1", 100, ["a"])
    assert bucket_by_tag_00912([p]) == {"a": ["s1"]}
