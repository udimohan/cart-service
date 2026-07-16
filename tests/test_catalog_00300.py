"""Tests for catalog_00300."""

import pytest

from cartservice.generated.catalog_00300 import (
    Product_00300,
    bucket_by_tag_00300,
    is_valid_sku_00300,
    price_with_tax_00300,
)


def test_price_with_tax_00300():
    assert price_with_tax_00300(1000, 500) == 1050


def test_price_with_tax_negative_00300():
    with pytest.raises(ValueError):
        price_with_tax_00300(1000, -1)


def test_is_valid_sku_00300():
    assert is_valid_sku_00300("abc123")
    assert not is_valid_sku_00300("")


def test_bucket_by_tag_00300():
    p = Product_00300("s1", 100, ["a"])
    assert bucket_by_tag_00300([p]) == {"a": ["s1"]}
