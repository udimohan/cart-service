"""Tests for catalog_00825."""

import pytest

from cartservice.generated.catalog_00825 import (
    Product_00825,
    bucket_by_tag_00825,
    is_valid_sku_00825,
    price_with_tax_00825,
)


def test_price_with_tax_00825():
    assert price_with_tax_00825(1000, 500) == 1050


def test_price_with_tax_negative_00825():
    with pytest.raises(ValueError):
        price_with_tax_00825(1000, -1)


def test_is_valid_sku_00825():
    assert is_valid_sku_00825("abc123")
    assert not is_valid_sku_00825("")


def test_bucket_by_tag_00825():
    p = Product_00825("s1", 100, ["a"])
    assert bucket_by_tag_00825([p]) == {"a": ["s1"]}
