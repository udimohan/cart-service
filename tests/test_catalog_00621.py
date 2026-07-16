"""Tests for catalog_00621."""

import pytest

from cartservice.generated.catalog_00621 import (
    Product_00621,
    bucket_by_tag_00621,
    is_valid_sku_00621,
    price_with_tax_00621,
)


def test_price_with_tax_00621():
    assert price_with_tax_00621(1000, 500) == 1050


def test_price_with_tax_negative_00621():
    with pytest.raises(ValueError):
        price_with_tax_00621(1000, -1)


def test_is_valid_sku_00621():
    assert is_valid_sku_00621("abc123")
    assert not is_valid_sku_00621("")


def test_bucket_by_tag_00621():
    p = Product_00621("s1", 100, ["a"])
    assert bucket_by_tag_00621([p]) == {"a": ["s1"]}
