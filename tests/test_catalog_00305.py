"""Tests for catalog_00305."""

import pytest

from cartservice.generated.catalog_00305 import (
    Product_00305,
    bucket_by_tag_00305,
    is_valid_sku_00305,
    price_with_tax_00305,
)


def test_price_with_tax_00305():
    assert price_with_tax_00305(1000, 500) == 1050


def test_price_with_tax_negative_00305():
    with pytest.raises(ValueError):
        price_with_tax_00305(1000, -1)


def test_is_valid_sku_00305():
    assert is_valid_sku_00305("abc123")
    assert not is_valid_sku_00305("")


def test_bucket_by_tag_00305():
    p = Product_00305("s1", 100, ["a"])
    assert bucket_by_tag_00305([p]) == {"a": ["s1"]}
