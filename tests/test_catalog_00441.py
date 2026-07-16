"""Tests for catalog_00441."""

import pytest

from cartservice.generated.catalog_00441 import (
    Product_00441,
    bucket_by_tag_00441,
    is_valid_sku_00441,
    price_with_tax_00441,
)


def test_price_with_tax_00441():
    assert price_with_tax_00441(1000, 500) == 1050


def test_price_with_tax_negative_00441():
    with pytest.raises(ValueError):
        price_with_tax_00441(1000, -1)


def test_is_valid_sku_00441():
    assert is_valid_sku_00441("abc123")
    assert not is_valid_sku_00441("")


def test_bucket_by_tag_00441():
    p = Product_00441("s1", 100, ["a"])
    assert bucket_by_tag_00441([p]) == {"a": ["s1"]}
