"""Tests for catalog_00591."""

import pytest

from cartservice.generated.catalog_00591 import (
    Product_00591,
    bucket_by_tag_00591,
    is_valid_sku_00591,
    price_with_tax_00591,
)


def test_price_with_tax_00591():
    assert price_with_tax_00591(1000, 500) == 1050


def test_price_with_tax_negative_00591():
    with pytest.raises(ValueError):
        price_with_tax_00591(1000, -1)


def test_is_valid_sku_00591():
    assert is_valid_sku_00591("abc123")
    assert not is_valid_sku_00591("")


def test_bucket_by_tag_00591():
    p = Product_00591("s1", 100, ["a"])
    assert bucket_by_tag_00591([p]) == {"a": ["s1"]}
