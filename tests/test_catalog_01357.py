"""Tests for catalog_01357."""

import pytest

from cartservice.generated.catalog_01357 import (
    Product_01357,
    bucket_by_tag_01357,
    is_valid_sku_01357,
    price_with_tax_01357,
)


def test_price_with_tax_01357():
    assert price_with_tax_01357(1000, 500) == 1050


def test_price_with_tax_negative_01357():
    with pytest.raises(ValueError):
        price_with_tax_01357(1000, -1)


def test_is_valid_sku_01357():
    assert is_valid_sku_01357("abc123")
    assert not is_valid_sku_01357("")


def test_bucket_by_tag_01357():
    p = Product_01357("s1", 100, ["a"])
    assert bucket_by_tag_01357([p]) == {"a": ["s1"]}
