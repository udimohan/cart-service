"""Tests for catalog_00337."""

import pytest

from cartservice.generated.catalog_00337 import (
    Product_00337,
    bucket_by_tag_00337,
    is_valid_sku_00337,
    price_with_tax_00337,
)


def test_price_with_tax_00337():
    assert price_with_tax_00337(1000, 500) == 1050


def test_price_with_tax_negative_00337():
    with pytest.raises(ValueError):
        price_with_tax_00337(1000, -1)


def test_is_valid_sku_00337():
    assert is_valid_sku_00337("abc123")
    assert not is_valid_sku_00337("")


def test_bucket_by_tag_00337():
    p = Product_00337("s1", 100, ["a"])
    assert bucket_by_tag_00337([p]) == {"a": ["s1"]}
