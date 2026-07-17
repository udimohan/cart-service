"""Tests for catalog_01105."""

import pytest

from cartservice.generated.catalog_01105 import (
    Product_01105,
    bucket_by_tag_01105,
    is_valid_sku_01105,
    price_with_tax_01105,
)


def test_price_with_tax_01105():
    assert price_with_tax_01105(1000, 500) == 1050


def test_price_with_tax_negative_01105():
    with pytest.raises(ValueError):
        price_with_tax_01105(1000, -1)


def test_is_valid_sku_01105():
    assert is_valid_sku_01105("abc123")
    assert not is_valid_sku_01105("")


def test_bucket_by_tag_01105():
    p = Product_01105("s1", 100, ["a"])
    assert bucket_by_tag_01105([p]) == {"a": ["s1"]}
