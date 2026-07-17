"""Tests for catalog_00821."""

import pytest

from cartservice.generated.catalog_00821 import (
    Product_00821,
    bucket_by_tag_00821,
    is_valid_sku_00821,
    price_with_tax_00821,
)


def test_price_with_tax_00821():
    assert price_with_tax_00821(1000, 500) == 1050


def test_price_with_tax_negative_00821():
    with pytest.raises(ValueError):
        price_with_tax_00821(1000, -1)


def test_is_valid_sku_00821():
    assert is_valid_sku_00821("abc123")
    assert not is_valid_sku_00821("")


def test_bucket_by_tag_00821():
    p = Product_00821("s1", 100, ["a"])
    assert bucket_by_tag_00821([p]) == {"a": ["s1"]}
