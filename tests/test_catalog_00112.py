"""Tests for catalog_00112."""

import pytest

from cartservice.generated.catalog_00112 import (
    Product_00112,
    bucket_by_tag_00112,
    is_valid_sku_00112,
    price_with_tax_00112,
)


def test_price_with_tax_00112():
    assert price_with_tax_00112(1000, 500) == 1050


def test_price_with_tax_negative_00112():
    with pytest.raises(ValueError):
        price_with_tax_00112(1000, -1)


def test_is_valid_sku_00112():
    assert is_valid_sku_00112("abc123")
    assert not is_valid_sku_00112("")


def test_bucket_by_tag_00112():
    p = Product_00112("s1", 100, ["a"])
    assert bucket_by_tag_00112([p]) == {"a": ["s1"]}
