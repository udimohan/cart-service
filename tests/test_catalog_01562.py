"""Tests for catalog_01562."""

import pytest

from cartservice.generated.catalog_01562 import (
    Product_01562,
    bucket_by_tag_01562,
    is_valid_sku_01562,
    price_with_tax_01562,
)


def test_price_with_tax_01562():
    assert price_with_tax_01562(1000, 500) == 1050


def test_price_with_tax_negative_01562():
    with pytest.raises(ValueError):
        price_with_tax_01562(1000, -1)


def test_is_valid_sku_01562():
    assert is_valid_sku_01562("abc123")
    assert not is_valid_sku_01562("")


def test_bucket_by_tag_01562():
    p = Product_01562("s1", 100, ["a"])
    assert bucket_by_tag_01562([p]) == {"a": ["s1"]}
