"""Tests for catalog_01077."""

import pytest

from cartservice.generated.catalog_01077 import (
    Product_01077,
    bucket_by_tag_01077,
    is_valid_sku_01077,
    price_with_tax_01077,
)


def test_price_with_tax_01077():
    assert price_with_tax_01077(1000, 500) == 1050


def test_price_with_tax_negative_01077():
    with pytest.raises(ValueError):
        price_with_tax_01077(1000, -1)


def test_is_valid_sku_01077():
    assert is_valid_sku_01077("abc123")
    assert not is_valid_sku_01077("")


def test_bucket_by_tag_01077():
    p = Product_01077("s1", 100, ["a"])
    assert bucket_by_tag_01077([p]) == {"a": ["s1"]}
