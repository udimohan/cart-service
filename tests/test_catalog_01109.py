"""Tests for catalog_01109."""

import pytest

from cartservice.generated.catalog_01109 import (
    Product_01109,
    bucket_by_tag_01109,
    is_valid_sku_01109,
    price_with_tax_01109,
)


def test_price_with_tax_01109():
    assert price_with_tax_01109(1000, 500) == 1050


def test_price_with_tax_negative_01109():
    with pytest.raises(ValueError):
        price_with_tax_01109(1000, -1)


def test_is_valid_sku_01109():
    assert is_valid_sku_01109("abc123")
    assert not is_valid_sku_01109("")


def test_bucket_by_tag_01109():
    p = Product_01109("s1", 100, ["a"])
    assert bucket_by_tag_01109([p]) == {"a": ["s1"]}
