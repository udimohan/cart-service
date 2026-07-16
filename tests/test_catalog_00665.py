"""Tests for catalog_00665."""

import pytest

from cartservice.generated.catalog_00665 import (
    Product_00665,
    bucket_by_tag_00665,
    is_valid_sku_00665,
    price_with_tax_00665,
)


def test_price_with_tax_00665():
    assert price_with_tax_00665(1000, 500) == 1050


def test_price_with_tax_negative_00665():
    with pytest.raises(ValueError):
        price_with_tax_00665(1000, -1)


def test_is_valid_sku_00665():
    assert is_valid_sku_00665("abc123")
    assert not is_valid_sku_00665("")


def test_bucket_by_tag_00665():
    p = Product_00665("s1", 100, ["a"])
    assert bucket_by_tag_00665([p]) == {"a": ["s1"]}
