"""Tests for catalog_01143."""

import pytest

from cartservice.generated.catalog_01143 import (
    Product_01143,
    bucket_by_tag_01143,
    is_valid_sku_01143,
    price_with_tax_01143,
)


def test_price_with_tax_01143():
    assert price_with_tax_01143(1000, 500) == 1050


def test_price_with_tax_negative_01143():
    with pytest.raises(ValueError):
        price_with_tax_01143(1000, -1)


def test_is_valid_sku_01143():
    assert is_valid_sku_01143("abc123")
    assert not is_valid_sku_01143("")


def test_bucket_by_tag_01143():
    p = Product_01143("s1", 100, ["a"])
    assert bucket_by_tag_01143([p]) == {"a": ["s1"]}
