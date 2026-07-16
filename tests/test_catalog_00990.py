"""Tests for catalog_00990."""

import pytest

from cartservice.generated.catalog_00990 import (
    Product_00990,
    bucket_by_tag_00990,
    is_valid_sku_00990,
    price_with_tax_00990,
)


def test_price_with_tax_00990():
    assert price_with_tax_00990(1000, 500) == 1050


def test_price_with_tax_negative_00990():
    with pytest.raises(ValueError):
        price_with_tax_00990(1000, -1)


def test_is_valid_sku_00990():
    assert is_valid_sku_00990("abc123")
    assert not is_valid_sku_00990("")


def test_bucket_by_tag_00990():
    p = Product_00990("s1", 100, ["a"])
    assert bucket_by_tag_00990([p]) == {"a": ["s1"]}
