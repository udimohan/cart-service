"""Tests for catalog_00662."""

import pytest

from cartservice.generated.catalog_00662 import (
    Product_00662,
    bucket_by_tag_00662,
    is_valid_sku_00662,
    price_with_tax_00662,
)


def test_price_with_tax_00662():
    assert price_with_tax_00662(1000, 500) == 1050


def test_price_with_tax_negative_00662():
    with pytest.raises(ValueError):
        price_with_tax_00662(1000, -1)


def test_is_valid_sku_00662():
    assert is_valid_sku_00662("abc123")
    assert not is_valid_sku_00662("")


def test_bucket_by_tag_00662():
    p = Product_00662("s1", 100, ["a"])
    assert bucket_by_tag_00662([p]) == {"a": ["s1"]}
