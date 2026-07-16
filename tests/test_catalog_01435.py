"""Tests for catalog_01435."""

import pytest

from cartservice.generated.catalog_01435 import (
    Product_01435,
    bucket_by_tag_01435,
    is_valid_sku_01435,
    price_with_tax_01435,
)


def test_price_with_tax_01435():
    assert price_with_tax_01435(1000, 500) == 1050


def test_price_with_tax_negative_01435():
    with pytest.raises(ValueError):
        price_with_tax_01435(1000, -1)


def test_is_valid_sku_01435():
    assert is_valid_sku_01435("abc123")
    assert not is_valid_sku_01435("")


def test_bucket_by_tag_01435():
    p = Product_01435("s1", 100, ["a"])
    assert bucket_by_tag_01435([p]) == {"a": ["s1"]}
