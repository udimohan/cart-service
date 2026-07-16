"""Tests for catalog_01580."""

import pytest

from cartservice.generated.catalog_01580 import (
    Product_01580,
    bucket_by_tag_01580,
    is_valid_sku_01580,
    price_with_tax_01580,
)


def test_price_with_tax_01580():
    assert price_with_tax_01580(1000, 500) == 1050


def test_price_with_tax_negative_01580():
    with pytest.raises(ValueError):
        price_with_tax_01580(1000, -1)


def test_is_valid_sku_01580():
    assert is_valid_sku_01580("abc123")
    assert not is_valid_sku_01580("")


def test_bucket_by_tag_01580():
    p = Product_01580("s1", 100, ["a"])
    assert bucket_by_tag_01580([p]) == {"a": ["s1"]}
