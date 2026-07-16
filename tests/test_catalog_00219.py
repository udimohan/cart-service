"""Tests for catalog_00219."""

import pytest

from cartservice.generated.catalog_00219 import (
    Product_00219,
    bucket_by_tag_00219,
    is_valid_sku_00219,
    price_with_tax_00219,
)


def test_price_with_tax_00219():
    assert price_with_tax_00219(1000, 500) == 1050


def test_price_with_tax_negative_00219():
    with pytest.raises(ValueError):
        price_with_tax_00219(1000, -1)


def test_is_valid_sku_00219():
    assert is_valid_sku_00219("abc123")
    assert not is_valid_sku_00219("")


def test_bucket_by_tag_00219():
    p = Product_00219("s1", 100, ["a"])
    assert bucket_by_tag_00219([p]) == {"a": ["s1"]}
