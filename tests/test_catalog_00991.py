"""Tests for catalog_00991."""

import pytest

from cartservice.generated.catalog_00991 import (
    Product_00991,
    bucket_by_tag_00991,
    is_valid_sku_00991,
    price_with_tax_00991,
)


def test_price_with_tax_00991():
    assert price_with_tax_00991(1000, 500) == 1050


def test_price_with_tax_negative_00991():
    with pytest.raises(ValueError):
        price_with_tax_00991(1000, -1)


def test_is_valid_sku_00991():
    assert is_valid_sku_00991("abc123")
    assert not is_valid_sku_00991("")


def test_bucket_by_tag_00991():
    p = Product_00991("s1", 100, ["a"])
    assert bucket_by_tag_00991([p]) == {"a": ["s1"]}
