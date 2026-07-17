"""Tests for catalog_00486."""

import pytest

from cartservice.generated.catalog_00486 import (
    Product_00486,
    bucket_by_tag_00486,
    is_valid_sku_00486,
    price_with_tax_00486,
)


def test_price_with_tax_00486():
    assert price_with_tax_00486(1000, 500) == 1050


def test_price_with_tax_negative_00486():
    with pytest.raises(ValueError):
        price_with_tax_00486(1000, -1)


def test_is_valid_sku_00486():
    assert is_valid_sku_00486("abc123")
    assert not is_valid_sku_00486("")


def test_bucket_by_tag_00486():
    p = Product_00486("s1", 100, ["a"])
    assert bucket_by_tag_00486([p]) == {"a": ["s1"]}
