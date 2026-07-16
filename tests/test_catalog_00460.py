"""Tests for catalog_00460."""

import pytest

from cartservice.generated.catalog_00460 import (
    Product_00460,
    bucket_by_tag_00460,
    is_valid_sku_00460,
    price_with_tax_00460,
)


def test_price_with_tax_00460():
    assert price_with_tax_00460(1000, 500) == 1050


def test_price_with_tax_negative_00460():
    with pytest.raises(ValueError):
        price_with_tax_00460(1000, -1)


def test_is_valid_sku_00460():
    assert is_valid_sku_00460("abc123")
    assert not is_valid_sku_00460("")


def test_bucket_by_tag_00460():
    p = Product_00460("s1", 100, ["a"])
    assert bucket_by_tag_00460([p]) == {"a": ["s1"]}
