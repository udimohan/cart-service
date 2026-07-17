"""Tests for catalog_00934."""

import pytest

from cartservice.generated.catalog_00934 import (
    Product_00934,
    bucket_by_tag_00934,
    is_valid_sku_00934,
    price_with_tax_00934,
)


def test_price_with_tax_00934():
    assert price_with_tax_00934(1000, 500) == 1050


def test_price_with_tax_negative_00934():
    with pytest.raises(ValueError):
        price_with_tax_00934(1000, -1)


def test_is_valid_sku_00934():
    assert is_valid_sku_00934("abc123")
    assert not is_valid_sku_00934("")


def test_bucket_by_tag_00934():
    p = Product_00934("s1", 100, ["a"])
    assert bucket_by_tag_00934([p]) == {"a": ["s1"]}
