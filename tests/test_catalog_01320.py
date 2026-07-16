"""Tests for catalog_01320."""

import pytest

from cartservice.generated.catalog_01320 import (
    Product_01320,
    bucket_by_tag_01320,
    is_valid_sku_01320,
    price_with_tax_01320,
)


def test_price_with_tax_01320():
    assert price_with_tax_01320(1000, 500) == 1050


def test_price_with_tax_negative_01320():
    with pytest.raises(ValueError):
        price_with_tax_01320(1000, -1)


def test_is_valid_sku_01320():
    assert is_valid_sku_01320("abc123")
    assert not is_valid_sku_01320("")


def test_bucket_by_tag_01320():
    p = Product_01320("s1", 100, ["a"])
    assert bucket_by_tag_01320([p]) == {"a": ["s1"]}
