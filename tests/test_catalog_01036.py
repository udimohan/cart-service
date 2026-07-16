"""Tests for catalog_01036."""

import pytest

from cartservice.generated.catalog_01036 import (
    Product_01036,
    bucket_by_tag_01036,
    is_valid_sku_01036,
    price_with_tax_01036,
)


def test_price_with_tax_01036():
    assert price_with_tax_01036(1000, 500) == 1050


def test_price_with_tax_negative_01036():
    with pytest.raises(ValueError):
        price_with_tax_01036(1000, -1)


def test_is_valid_sku_01036():
    assert is_valid_sku_01036("abc123")
    assert not is_valid_sku_01036("")


def test_bucket_by_tag_01036():
    p = Product_01036("s1", 100, ["a"])
    assert bucket_by_tag_01036([p]) == {"a": ["s1"]}
