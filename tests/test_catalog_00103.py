"""Tests for catalog_00103."""

import pytest

from cartservice.generated.catalog_00103 import (
    Product_00103,
    bucket_by_tag_00103,
    is_valid_sku_00103,
    price_with_tax_00103,
)


def test_price_with_tax_00103():
    assert price_with_tax_00103(1000, 500) == 1050


def test_price_with_tax_negative_00103():
    with pytest.raises(ValueError):
        price_with_tax_00103(1000, -1)


def test_is_valid_sku_00103():
    assert is_valid_sku_00103("abc123")
    assert not is_valid_sku_00103("")


def test_bucket_by_tag_00103():
    p = Product_00103("s1", 100, ["a"])
    assert bucket_by_tag_00103([p]) == {"a": ["s1"]}
