"""Tests for catalog_00632."""

import pytest

from cartservice.generated.catalog_00632 import (
    Product_00632,
    bucket_by_tag_00632,
    is_valid_sku_00632,
    price_with_tax_00632,
)


def test_price_with_tax_00632():
    assert price_with_tax_00632(1000, 500) == 1050


def test_price_with_tax_negative_00632():
    with pytest.raises(ValueError):
        price_with_tax_00632(1000, -1)


def test_is_valid_sku_00632():
    assert is_valid_sku_00632("abc123")
    assert not is_valid_sku_00632("")


def test_bucket_by_tag_00632():
    p = Product_00632("s1", 100, ["a"])
    assert bucket_by_tag_00632([p]) == {"a": ["s1"]}
