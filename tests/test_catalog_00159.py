"""Tests for catalog_00159."""

import pytest

from cartservice.generated.catalog_00159 import (
    Product_00159,
    bucket_by_tag_00159,
    is_valid_sku_00159,
    price_with_tax_00159,
)


def test_price_with_tax_00159():
    assert price_with_tax_00159(1000, 500) == 1050


def test_price_with_tax_negative_00159():
    with pytest.raises(ValueError):
        price_with_tax_00159(1000, -1)


def test_is_valid_sku_00159():
    assert is_valid_sku_00159("abc123")
    assert not is_valid_sku_00159("")


def test_bucket_by_tag_00159():
    p = Product_00159("s1", 100, ["a"])
    assert bucket_by_tag_00159([p]) == {"a": ["s1"]}
