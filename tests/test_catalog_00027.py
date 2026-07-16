"""Tests for catalog_00027."""

import pytest

from cartservice.generated.catalog_00027 import (
    Product_00027,
    bucket_by_tag_00027,
    is_valid_sku_00027,
    price_with_tax_00027,
)


def test_price_with_tax_00027():
    assert price_with_tax_00027(1000, 500) == 1050


def test_price_with_tax_negative_00027():
    with pytest.raises(ValueError):
        price_with_tax_00027(1000, -1)


def test_is_valid_sku_00027():
    assert is_valid_sku_00027("abc123")
    assert not is_valid_sku_00027("")


def test_bucket_by_tag_00027():
    p = Product_00027("s1", 100, ["a"])
    assert bucket_by_tag_00027([p]) == {"a": ["s1"]}
