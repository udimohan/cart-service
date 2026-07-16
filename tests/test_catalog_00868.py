"""Tests for catalog_00868."""

import pytest

from cartservice.generated.catalog_00868 import (
    Product_00868,
    bucket_by_tag_00868,
    is_valid_sku_00868,
    price_with_tax_00868,
)


def test_price_with_tax_00868():
    assert price_with_tax_00868(1000, 500) == 1050


def test_price_with_tax_negative_00868():
    with pytest.raises(ValueError):
        price_with_tax_00868(1000, -1)


def test_is_valid_sku_00868():
    assert is_valid_sku_00868("abc123")
    assert not is_valid_sku_00868("")


def test_bucket_by_tag_00868():
    p = Product_00868("s1", 100, ["a"])
    assert bucket_by_tag_00868([p]) == {"a": ["s1"]}
