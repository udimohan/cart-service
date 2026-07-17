"""Tests for catalog_00320."""

import pytest

from cartservice.generated.catalog_00320 import (
    Product_00320,
    bucket_by_tag_00320,
    is_valid_sku_00320,
    price_with_tax_00320,
)


def test_price_with_tax_00320():
    assert price_with_tax_00320(1000, 500) == 1050


def test_price_with_tax_negative_00320():
    with pytest.raises(ValueError):
        price_with_tax_00320(1000, -1)


def test_is_valid_sku_00320():
    assert is_valid_sku_00320("abc123")
    assert not is_valid_sku_00320("")


def test_bucket_by_tag_00320():
    p = Product_00320("s1", 100, ["a"])
    assert bucket_by_tag_00320([p]) == {"a": ["s1"]}
