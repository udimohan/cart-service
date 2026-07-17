"""Tests for catalog_01468."""

import pytest

from cartservice.generated.catalog_01468 import (
    Product_01468,
    bucket_by_tag_01468,
    is_valid_sku_01468,
    price_with_tax_01468,
)


def test_price_with_tax_01468():
    assert price_with_tax_01468(1000, 500) == 1050


def test_price_with_tax_negative_01468():
    with pytest.raises(ValueError):
        price_with_tax_01468(1000, -1)


def test_is_valid_sku_01468():
    assert is_valid_sku_01468("abc123")
    assert not is_valid_sku_01468("")


def test_bucket_by_tag_01468():
    p = Product_01468("s1", 100, ["a"])
    assert bucket_by_tag_01468([p]) == {"a": ["s1"]}
