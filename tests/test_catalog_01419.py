"""Tests for catalog_01419."""

import pytest

from cartservice.generated.catalog_01419 import (
    Product_01419,
    bucket_by_tag_01419,
    is_valid_sku_01419,
    price_with_tax_01419,
)


def test_price_with_tax_01419():
    assert price_with_tax_01419(1000, 500) == 1050


def test_price_with_tax_negative_01419():
    with pytest.raises(ValueError):
        price_with_tax_01419(1000, -1)


def test_is_valid_sku_01419():
    assert is_valid_sku_01419("abc123")
    assert not is_valid_sku_01419("")


def test_bucket_by_tag_01419():
    p = Product_01419("s1", 100, ["a"])
    assert bucket_by_tag_01419([p]) == {"a": ["s1"]}
