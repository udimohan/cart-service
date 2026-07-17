"""Tests for catalog_00042."""

import pytest

from cartservice.generated.catalog_00042 import (
    Product_00042,
    bucket_by_tag_00042,
    is_valid_sku_00042,
    price_with_tax_00042,
)


def test_price_with_tax_00042():
    assert price_with_tax_00042(1000, 500) == 1050


def test_price_with_tax_negative_00042():
    with pytest.raises(ValueError):
        price_with_tax_00042(1000, -1)


def test_is_valid_sku_00042():
    assert is_valid_sku_00042("abc123")
    assert not is_valid_sku_00042("")


def test_bucket_by_tag_00042():
    p = Product_00042("s1", 100, ["a"])
    assert bucket_by_tag_00042([p]) == {"a": ["s1"]}
