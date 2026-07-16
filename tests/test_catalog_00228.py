"""Tests for catalog_00228."""

import pytest

from cartservice.generated.catalog_00228 import (
    Product_00228,
    bucket_by_tag_00228,
    is_valid_sku_00228,
    price_with_tax_00228,
)


def test_price_with_tax_00228():
    assert price_with_tax_00228(1000, 500) == 1050


def test_price_with_tax_negative_00228():
    with pytest.raises(ValueError):
        price_with_tax_00228(1000, -1)


def test_is_valid_sku_00228():
    assert is_valid_sku_00228("abc123")
    assert not is_valid_sku_00228("")


def test_bucket_by_tag_00228():
    p = Product_00228("s1", 100, ["a"])
    assert bucket_by_tag_00228([p]) == {"a": ["s1"]}
