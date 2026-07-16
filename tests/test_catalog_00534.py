"""Tests for catalog_00534."""

import pytest

from cartservice.generated.catalog_00534 import (
    Product_00534,
    bucket_by_tag_00534,
    is_valid_sku_00534,
    price_with_tax_00534,
)


def test_price_with_tax_00534():
    assert price_with_tax_00534(1000, 500) == 1050


def test_price_with_tax_negative_00534():
    with pytest.raises(ValueError):
        price_with_tax_00534(1000, -1)


def test_is_valid_sku_00534():
    assert is_valid_sku_00534("abc123")
    assert not is_valid_sku_00534("")


def test_bucket_by_tag_00534():
    p = Product_00534("s1", 100, ["a"])
    assert bucket_by_tag_00534([p]) == {"a": ["s1"]}
