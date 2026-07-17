"""Tests for catalog_01184."""

import pytest

from cartservice.generated.catalog_01184 import (
    Product_01184,
    bucket_by_tag_01184,
    is_valid_sku_01184,
    price_with_tax_01184,
)


def test_price_with_tax_01184():
    assert price_with_tax_01184(1000, 500) == 1050


def test_price_with_tax_negative_01184():
    with pytest.raises(ValueError):
        price_with_tax_01184(1000, -1)


def test_is_valid_sku_01184():
    assert is_valid_sku_01184("abc123")
    assert not is_valid_sku_01184("")


def test_bucket_by_tag_01184():
    p = Product_01184("s1", 100, ["a"])
    assert bucket_by_tag_01184([p]) == {"a": ["s1"]}
