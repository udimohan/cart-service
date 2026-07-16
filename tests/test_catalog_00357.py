"""Tests for catalog_00357."""

import pytest

from cartservice.generated.catalog_00357 import (
    Product_00357,
    bucket_by_tag_00357,
    is_valid_sku_00357,
    price_with_tax_00357,
)


def test_price_with_tax_00357():
    assert price_with_tax_00357(1000, 500) == 1050


def test_price_with_tax_negative_00357():
    with pytest.raises(ValueError):
        price_with_tax_00357(1000, -1)


def test_is_valid_sku_00357():
    assert is_valid_sku_00357("abc123")
    assert not is_valid_sku_00357("")


def test_bucket_by_tag_00357():
    p = Product_00357("s1", 100, ["a"])
    assert bucket_by_tag_00357([p]) == {"a": ["s1"]}
