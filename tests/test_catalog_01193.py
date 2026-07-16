"""Tests for catalog_01193."""

import pytest

from cartservice.generated.catalog_01193 import (
    Product_01193,
    bucket_by_tag_01193,
    is_valid_sku_01193,
    price_with_tax_01193,
)


def test_price_with_tax_01193():
    assert price_with_tax_01193(1000, 500) == 1050


def test_price_with_tax_negative_01193():
    with pytest.raises(ValueError):
        price_with_tax_01193(1000, -1)


def test_is_valid_sku_01193():
    assert is_valid_sku_01193("abc123")
    assert not is_valid_sku_01193("")


def test_bucket_by_tag_01193():
    p = Product_01193("s1", 100, ["a"])
    assert bucket_by_tag_01193([p]) == {"a": ["s1"]}
