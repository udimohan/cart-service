"""Tests for catalog_00176."""

import pytest

from cartservice.generated.catalog_00176 import (
    Product_00176,
    bucket_by_tag_00176,
    is_valid_sku_00176,
    price_with_tax_00176,
)


def test_price_with_tax_00176():
    assert price_with_tax_00176(1000, 500) == 1050


def test_price_with_tax_negative_00176():
    with pytest.raises(ValueError):
        price_with_tax_00176(1000, -1)


def test_is_valid_sku_00176():
    assert is_valid_sku_00176("abc123")
    assert not is_valid_sku_00176("")


def test_bucket_by_tag_00176():
    p = Product_00176("s1", 100, ["a"])
    assert bucket_by_tag_00176([p]) == {"a": ["s1"]}
