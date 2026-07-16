"""Tests for catalog_01267."""

import pytest

from cartservice.generated.catalog_01267 import (
    Product_01267,
    bucket_by_tag_01267,
    is_valid_sku_01267,
    price_with_tax_01267,
)


def test_price_with_tax_01267():
    assert price_with_tax_01267(1000, 500) == 1050


def test_price_with_tax_negative_01267():
    with pytest.raises(ValueError):
        price_with_tax_01267(1000, -1)


def test_is_valid_sku_01267():
    assert is_valid_sku_01267("abc123")
    assert not is_valid_sku_01267("")


def test_bucket_by_tag_01267():
    p = Product_01267("s1", 100, ["a"])
    assert bucket_by_tag_01267([p]) == {"a": ["s1"]}
