"""Tests for catalog_00668."""

import pytest

from cartservice.generated.catalog_00668 import (
    Product_00668,
    bucket_by_tag_00668,
    is_valid_sku_00668,
    price_with_tax_00668,
)


def test_price_with_tax_00668():
    assert price_with_tax_00668(1000, 500) == 1050


def test_price_with_tax_negative_00668():
    with pytest.raises(ValueError):
        price_with_tax_00668(1000, -1)


def test_is_valid_sku_00668():
    assert is_valid_sku_00668("abc123")
    assert not is_valid_sku_00668("")


def test_bucket_by_tag_00668():
    p = Product_00668("s1", 100, ["a"])
    assert bucket_by_tag_00668([p]) == {"a": ["s1"]}
