"""Tests for catalog_01456."""

import pytest

from cartservice.generated.catalog_01456 import (
    Product_01456,
    bucket_by_tag_01456,
    is_valid_sku_01456,
    price_with_tax_01456,
)


def test_price_with_tax_01456():
    assert price_with_tax_01456(1000, 500) == 1050


def test_price_with_tax_negative_01456():
    with pytest.raises(ValueError):
        price_with_tax_01456(1000, -1)


def test_is_valid_sku_01456():
    assert is_valid_sku_01456("abc123")
    assert not is_valid_sku_01456("")


def test_bucket_by_tag_01456():
    p = Product_01456("s1", 100, ["a"])
    assert bucket_by_tag_01456([p]) == {"a": ["s1"]}
