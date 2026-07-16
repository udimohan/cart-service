"""Tests for catalog_01525."""

import pytest

from cartservice.generated.catalog_01525 import (
    Product_01525,
    bucket_by_tag_01525,
    is_valid_sku_01525,
    price_with_tax_01525,
)


def test_price_with_tax_01525():
    assert price_with_tax_01525(1000, 500) == 1050


def test_price_with_tax_negative_01525():
    with pytest.raises(ValueError):
        price_with_tax_01525(1000, -1)


def test_is_valid_sku_01525():
    assert is_valid_sku_01525("abc123")
    assert not is_valid_sku_01525("")


def test_bucket_by_tag_01525():
    p = Product_01525("s1", 100, ["a"])
    assert bucket_by_tag_01525([p]) == {"a": ["s1"]}
