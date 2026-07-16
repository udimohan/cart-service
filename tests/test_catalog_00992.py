"""Tests for catalog_00992."""

import pytest

from cartservice.generated.catalog_00992 import (
    Product_00992,
    bucket_by_tag_00992,
    is_valid_sku_00992,
    price_with_tax_00992,
)


def test_price_with_tax_00992():
    assert price_with_tax_00992(1000, 500) == 1050


def test_price_with_tax_negative_00992():
    with pytest.raises(ValueError):
        price_with_tax_00992(1000, -1)


def test_is_valid_sku_00992():
    assert is_valid_sku_00992("abc123")
    assert not is_valid_sku_00992("")


def test_bucket_by_tag_00992():
    p = Product_00992("s1", 100, ["a"])
    assert bucket_by_tag_00992([p]) == {"a": ["s1"]}
