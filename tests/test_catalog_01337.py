"""Tests for catalog_01337."""

import pytest

from cartservice.generated.catalog_01337 import (
    Product_01337,
    bucket_by_tag_01337,
    is_valid_sku_01337,
    price_with_tax_01337,
)


def test_price_with_tax_01337():
    assert price_with_tax_01337(1000, 500) == 1050


def test_price_with_tax_negative_01337():
    with pytest.raises(ValueError):
        price_with_tax_01337(1000, -1)


def test_is_valid_sku_01337():
    assert is_valid_sku_01337("abc123")
    assert not is_valid_sku_01337("")


def test_bucket_by_tag_01337():
    p = Product_01337("s1", 100, ["a"])
    assert bucket_by_tag_01337([p]) == {"a": ["s1"]}
