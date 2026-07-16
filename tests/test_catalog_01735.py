"""Tests for catalog_01735."""

import pytest

from cartservice.generated.catalog_01735 import (
    Product_01735,
    bucket_by_tag_01735,
    is_valid_sku_01735,
    price_with_tax_01735,
)


def test_price_with_tax_01735():
    assert price_with_tax_01735(1000, 500) == 1050


def test_price_with_tax_negative_01735():
    with pytest.raises(ValueError):
        price_with_tax_01735(1000, -1)


def test_is_valid_sku_01735():
    assert is_valid_sku_01735("abc123")
    assert not is_valid_sku_01735("")


def test_bucket_by_tag_01735():
    p = Product_01735("s1", 100, ["a"])
    assert bucket_by_tag_01735([p]) == {"a": ["s1"]}
