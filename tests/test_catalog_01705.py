"""Tests for catalog_01705."""

import pytest

from cartservice.generated.catalog_01705 import (
    Product_01705,
    bucket_by_tag_01705,
    is_valid_sku_01705,
    price_with_tax_01705,
)


def test_price_with_tax_01705():
    assert price_with_tax_01705(1000, 500) == 1050


def test_price_with_tax_negative_01705():
    with pytest.raises(ValueError):
        price_with_tax_01705(1000, -1)


def test_is_valid_sku_01705():
    assert is_valid_sku_01705("abc123")
    assert not is_valid_sku_01705("")


def test_bucket_by_tag_01705():
    p = Product_01705("s1", 100, ["a"])
    assert bucket_by_tag_01705([p]) == {"a": ["s1"]}
