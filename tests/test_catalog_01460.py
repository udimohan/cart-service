"""Tests for catalog_01460."""

import pytest

from cartservice.generated.catalog_01460 import (
    Product_01460,
    bucket_by_tag_01460,
    is_valid_sku_01460,
    price_with_tax_01460,
)


def test_price_with_tax_01460():
    assert price_with_tax_01460(1000, 500) == 1050


def test_price_with_tax_negative_01460():
    with pytest.raises(ValueError):
        price_with_tax_01460(1000, -1)


def test_is_valid_sku_01460():
    assert is_valid_sku_01460("abc123")
    assert not is_valid_sku_01460("")


def test_bucket_by_tag_01460():
    p = Product_01460("s1", 100, ["a"])
    assert bucket_by_tag_01460([p]) == {"a": ["s1"]}
