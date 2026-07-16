"""Tests for catalog_01284."""

import pytest

from cartservice.generated.catalog_01284 import (
    Product_01284,
    bucket_by_tag_01284,
    is_valid_sku_01284,
    price_with_tax_01284,
)


def test_price_with_tax_01284():
    assert price_with_tax_01284(1000, 500) == 1050


def test_price_with_tax_negative_01284():
    with pytest.raises(ValueError):
        price_with_tax_01284(1000, -1)


def test_is_valid_sku_01284():
    assert is_valid_sku_01284("abc123")
    assert not is_valid_sku_01284("")


def test_bucket_by_tag_01284():
    p = Product_01284("s1", 100, ["a"])
    assert bucket_by_tag_01284([p]) == {"a": ["s1"]}
