"""Tests for catalog_01249."""

import pytest

from cartservice.generated.catalog_01249 import (
    Product_01249,
    bucket_by_tag_01249,
    is_valid_sku_01249,
    price_with_tax_01249,
)


def test_price_with_tax_01249():
    assert price_with_tax_01249(1000, 500) == 1050


def test_price_with_tax_negative_01249():
    with pytest.raises(ValueError):
        price_with_tax_01249(1000, -1)


def test_is_valid_sku_01249():
    assert is_valid_sku_01249("abc123")
    assert not is_valid_sku_01249("")


def test_bucket_by_tag_01249():
    p = Product_01249("s1", 100, ["a"])
    assert bucket_by_tag_01249([p]) == {"a": ["s1"]}
