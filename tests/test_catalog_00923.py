"""Tests for catalog_00923."""

import pytest

from cartservice.generated.catalog_00923 import (
    Product_00923,
    bucket_by_tag_00923,
    is_valid_sku_00923,
    price_with_tax_00923,
)


def test_price_with_tax_00923():
    assert price_with_tax_00923(1000, 500) == 1050


def test_price_with_tax_negative_00923():
    with pytest.raises(ValueError):
        price_with_tax_00923(1000, -1)


def test_is_valid_sku_00923():
    assert is_valid_sku_00923("abc123")
    assert not is_valid_sku_00923("")


def test_bucket_by_tag_00923():
    p = Product_00923("s1", 100, ["a"])
    assert bucket_by_tag_00923([p]) == {"a": ["s1"]}
