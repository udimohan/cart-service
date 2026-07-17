"""Tests for catalog_00850."""

import pytest

from cartservice.generated.catalog_00850 import (
    Product_00850,
    bucket_by_tag_00850,
    is_valid_sku_00850,
    price_with_tax_00850,
)


def test_price_with_tax_00850():
    assert price_with_tax_00850(1000, 500) == 1050


def test_price_with_tax_negative_00850():
    with pytest.raises(ValueError):
        price_with_tax_00850(1000, -1)


def test_is_valid_sku_00850():
    assert is_valid_sku_00850("abc123")
    assert not is_valid_sku_00850("")


def test_bucket_by_tag_00850():
    p = Product_00850("s1", 100, ["a"])
    assert bucket_by_tag_00850([p]) == {"a": ["s1"]}
