"""Tests for catalog_00524."""

import pytest

from cartservice.generated.catalog_00524 import (
    Product_00524,
    bucket_by_tag_00524,
    is_valid_sku_00524,
    price_with_tax_00524,
)


def test_price_with_tax_00524():
    assert price_with_tax_00524(1000, 500) == 1050


def test_price_with_tax_negative_00524():
    with pytest.raises(ValueError):
        price_with_tax_00524(1000, -1)


def test_is_valid_sku_00524():
    assert is_valid_sku_00524("abc123")
    assert not is_valid_sku_00524("")


def test_bucket_by_tag_00524():
    p = Product_00524("s1", 100, ["a"])
    assert bucket_by_tag_00524([p]) == {"a": ["s1"]}
