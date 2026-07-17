"""Tests for catalog_00004."""

import pytest

from cartservice.generated.catalog_00004 import (
    Product_00004,
    bucket_by_tag_00004,
    is_valid_sku_00004,
    price_with_tax_00004,
)


def test_price_with_tax_00004():
    assert price_with_tax_00004(1000, 500) == 1050


def test_price_with_tax_negative_00004():
    with pytest.raises(ValueError):
        price_with_tax_00004(1000, -1)


def test_is_valid_sku_00004():
    assert is_valid_sku_00004("abc123")
    assert not is_valid_sku_00004("")


def test_bucket_by_tag_00004():
    p = Product_00004("s1", 100, ["a"])
    assert bucket_by_tag_00004([p]) == {"a": ["s1"]}
