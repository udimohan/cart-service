"""Tests for catalog_00875."""

import pytest

from cartservice.generated.catalog_00875 import (
    Product_00875,
    bucket_by_tag_00875,
    is_valid_sku_00875,
    price_with_tax_00875,
)


def test_price_with_tax_00875():
    assert price_with_tax_00875(1000, 500) == 1050


def test_price_with_tax_negative_00875():
    with pytest.raises(ValueError):
        price_with_tax_00875(1000, -1)


def test_is_valid_sku_00875():
    assert is_valid_sku_00875("abc123")
    assert not is_valid_sku_00875("")


def test_bucket_by_tag_00875():
    p = Product_00875("s1", 100, ["a"])
    assert bucket_by_tag_00875([p]) == {"a": ["s1"]}
