"""Tests for catalog_01383."""

import pytest

from cartservice.generated.catalog_01383 import (
    Product_01383,
    bucket_by_tag_01383,
    is_valid_sku_01383,
    price_with_tax_01383,
)


def test_price_with_tax_01383():
    assert price_with_tax_01383(1000, 500) == 1050


def test_price_with_tax_negative_01383():
    with pytest.raises(ValueError):
        price_with_tax_01383(1000, -1)


def test_is_valid_sku_01383():
    assert is_valid_sku_01383("abc123")
    assert not is_valid_sku_01383("")


def test_bucket_by_tag_01383():
    p = Product_01383("s1", 100, ["a"])
    assert bucket_by_tag_01383([p]) == {"a": ["s1"]}
