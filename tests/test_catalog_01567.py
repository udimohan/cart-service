"""Tests for catalog_01567."""

import pytest

from cartservice.generated.catalog_01567 import (
    Product_01567,
    bucket_by_tag_01567,
    is_valid_sku_01567,
    price_with_tax_01567,
)


def test_price_with_tax_01567():
    assert price_with_tax_01567(1000, 500) == 1050


def test_price_with_tax_negative_01567():
    with pytest.raises(ValueError):
        price_with_tax_01567(1000, -1)


def test_is_valid_sku_01567():
    assert is_valid_sku_01567("abc123")
    assert not is_valid_sku_01567("")


def test_bucket_by_tag_01567():
    p = Product_01567("s1", 100, ["a"])
    assert bucket_by_tag_01567([p]) == {"a": ["s1"]}
