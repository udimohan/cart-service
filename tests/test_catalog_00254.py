"""Tests for catalog_00254."""

import pytest

from cartservice.generated.catalog_00254 import (
    Product_00254,
    bucket_by_tag_00254,
    is_valid_sku_00254,
    price_with_tax_00254,
)


def test_price_with_tax_00254():
    assert price_with_tax_00254(1000, 500) == 1050


def test_price_with_tax_negative_00254():
    with pytest.raises(ValueError):
        price_with_tax_00254(1000, -1)


def test_is_valid_sku_00254():
    assert is_valid_sku_00254("abc123")
    assert not is_valid_sku_00254("")


def test_bucket_by_tag_00254():
    p = Product_00254("s1", 100, ["a"])
    assert bucket_by_tag_00254([p]) == {"a": ["s1"]}
