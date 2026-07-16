"""Tests for catalog_00497."""

import pytest

from cartservice.generated.catalog_00497 import (
    Product_00497,
    bucket_by_tag_00497,
    is_valid_sku_00497,
    price_with_tax_00497,
)


def test_price_with_tax_00497():
    assert price_with_tax_00497(1000, 500) == 1050


def test_price_with_tax_negative_00497():
    with pytest.raises(ValueError):
        price_with_tax_00497(1000, -1)


def test_is_valid_sku_00497():
    assert is_valid_sku_00497("abc123")
    assert not is_valid_sku_00497("")


def test_bucket_by_tag_00497():
    p = Product_00497("s1", 100, ["a"])
    assert bucket_by_tag_00497([p]) == {"a": ["s1"]}
