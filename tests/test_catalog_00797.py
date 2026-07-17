"""Tests for catalog_00797."""

import pytest

from cartservice.generated.catalog_00797 import (
    Product_00797,
    bucket_by_tag_00797,
    is_valid_sku_00797,
    price_with_tax_00797,
)


def test_price_with_tax_00797():
    assert price_with_tax_00797(1000, 500) == 1050


def test_price_with_tax_negative_00797():
    with pytest.raises(ValueError):
        price_with_tax_00797(1000, -1)


def test_is_valid_sku_00797():
    assert is_valid_sku_00797("abc123")
    assert not is_valid_sku_00797("")


def test_bucket_by_tag_00797():
    p = Product_00797("s1", 100, ["a"])
    assert bucket_by_tag_00797([p]) == {"a": ["s1"]}
