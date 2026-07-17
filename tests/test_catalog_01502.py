"""Tests for catalog_01502."""

import pytest

from cartservice.generated.catalog_01502 import (
    Product_01502,
    bucket_by_tag_01502,
    is_valid_sku_01502,
    price_with_tax_01502,
)


def test_price_with_tax_01502():
    assert price_with_tax_01502(1000, 500) == 1050


def test_price_with_tax_negative_01502():
    with pytest.raises(ValueError):
        price_with_tax_01502(1000, -1)


def test_is_valid_sku_01502():
    assert is_valid_sku_01502("abc123")
    assert not is_valid_sku_01502("")


def test_bucket_by_tag_01502():
    p = Product_01502("s1", 100, ["a"])
    assert bucket_by_tag_01502([p]) == {"a": ["s1"]}
