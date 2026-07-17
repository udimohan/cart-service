"""Tests for catalog_01359."""

import pytest

from cartservice.generated.catalog_01359 import (
    Product_01359,
    bucket_by_tag_01359,
    is_valid_sku_01359,
    price_with_tax_01359,
)


def test_price_with_tax_01359():
    assert price_with_tax_01359(1000, 500) == 1050


def test_price_with_tax_negative_01359():
    with pytest.raises(ValueError):
        price_with_tax_01359(1000, -1)


def test_is_valid_sku_01359():
    assert is_valid_sku_01359("abc123")
    assert not is_valid_sku_01359("")


def test_bucket_by_tag_01359():
    p = Product_01359("s1", 100, ["a"])
    assert bucket_by_tag_01359([p]) == {"a": ["s1"]}
