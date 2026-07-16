"""Tests for catalog_01004."""

import pytest

from cartservice.generated.catalog_01004 import (
    Product_01004,
    bucket_by_tag_01004,
    is_valid_sku_01004,
    price_with_tax_01004,
)


def test_price_with_tax_01004():
    assert price_with_tax_01004(1000, 500) == 1050


def test_price_with_tax_negative_01004():
    with pytest.raises(ValueError):
        price_with_tax_01004(1000, -1)


def test_is_valid_sku_01004():
    assert is_valid_sku_01004("abc123")
    assert not is_valid_sku_01004("")


def test_bucket_by_tag_01004():
    p = Product_01004("s1", 100, ["a"])
    assert bucket_by_tag_01004([p]) == {"a": ["s1"]}
