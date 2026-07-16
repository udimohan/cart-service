"""Tests for catalog_00838."""

import pytest

from cartservice.generated.catalog_00838 import (
    Product_00838,
    bucket_by_tag_00838,
    is_valid_sku_00838,
    price_with_tax_00838,
)


def test_price_with_tax_00838():
    assert price_with_tax_00838(1000, 500) == 1050


def test_price_with_tax_negative_00838():
    with pytest.raises(ValueError):
        price_with_tax_00838(1000, -1)


def test_is_valid_sku_00838():
    assert is_valid_sku_00838("abc123")
    assert not is_valid_sku_00838("")


def test_bucket_by_tag_00838():
    p = Product_00838("s1", 100, ["a"])
    assert bucket_by_tag_00838([p]) == {"a": ["s1"]}
