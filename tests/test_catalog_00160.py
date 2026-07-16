"""Tests for catalog_00160."""

import pytest

from cartservice.generated.catalog_00160 import (
    Product_00160,
    bucket_by_tag_00160,
    is_valid_sku_00160,
    price_with_tax_00160,
)


def test_price_with_tax_00160():
    assert price_with_tax_00160(1000, 500) == 1050


def test_price_with_tax_negative_00160():
    with pytest.raises(ValueError):
        price_with_tax_00160(1000, -1)


def test_is_valid_sku_00160():
    assert is_valid_sku_00160("abc123")
    assert not is_valid_sku_00160("")


def test_bucket_by_tag_00160():
    p = Product_00160("s1", 100, ["a"])
    assert bucket_by_tag_00160([p]) == {"a": ["s1"]}
