"""Tests for catalog_01742."""

import pytest

from cartservice.generated.catalog_01742 import (
    Product_01742,
    bucket_by_tag_01742,
    is_valid_sku_01742,
    price_with_tax_01742,
)


def test_price_with_tax_01742():
    assert price_with_tax_01742(1000, 500) == 1050


def test_price_with_tax_negative_01742():
    with pytest.raises(ValueError):
        price_with_tax_01742(1000, -1)


def test_is_valid_sku_01742():
    assert is_valid_sku_01742("abc123")
    assert not is_valid_sku_01742("")


def test_bucket_by_tag_01742():
    p = Product_01742("s1", 100, ["a"])
    assert bucket_by_tag_01742([p]) == {"a": ["s1"]}
