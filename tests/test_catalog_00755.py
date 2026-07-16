"""Tests for catalog_00755."""

import pytest

from cartservice.generated.catalog_00755 import (
    Product_00755,
    bucket_by_tag_00755,
    is_valid_sku_00755,
    price_with_tax_00755,
)


def test_price_with_tax_00755():
    assert price_with_tax_00755(1000, 500) == 1050


def test_price_with_tax_negative_00755():
    with pytest.raises(ValueError):
        price_with_tax_00755(1000, -1)


def test_is_valid_sku_00755():
    assert is_valid_sku_00755("abc123")
    assert not is_valid_sku_00755("")


def test_bucket_by_tag_00755():
    p = Product_00755("s1", 100, ["a"])
    assert bucket_by_tag_00755([p]) == {"a": ["s1"]}
