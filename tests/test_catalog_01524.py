"""Tests for catalog_01524."""

import pytest

from cartservice.generated.catalog_01524 import (
    Product_01524,
    bucket_by_tag_01524,
    is_valid_sku_01524,
    price_with_tax_01524,
)


def test_price_with_tax_01524():
    assert price_with_tax_01524(1000, 500) == 1050


def test_price_with_tax_negative_01524():
    with pytest.raises(ValueError):
        price_with_tax_01524(1000, -1)


def test_is_valid_sku_01524():
    assert is_valid_sku_01524("abc123")
    assert not is_valid_sku_01524("")


def test_bucket_by_tag_01524():
    p = Product_01524("s1", 100, ["a"])
    assert bucket_by_tag_01524([p]) == {"a": ["s1"]}
