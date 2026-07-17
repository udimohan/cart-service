"""Tests for catalog_00090."""

import pytest

from cartservice.generated.catalog_00090 import (
    Product_00090,
    bucket_by_tag_00090,
    is_valid_sku_00090,
    price_with_tax_00090,
)


def test_price_with_tax_00090():
    assert price_with_tax_00090(1000, 500) == 1050


def test_price_with_tax_negative_00090():
    with pytest.raises(ValueError):
        price_with_tax_00090(1000, -1)


def test_is_valid_sku_00090():
    assert is_valid_sku_00090("abc123")
    assert not is_valid_sku_00090("")


def test_bucket_by_tag_00090():
    p = Product_00090("s1", 100, ["a"])
    assert bucket_by_tag_00090([p]) == {"a": ["s1"]}
