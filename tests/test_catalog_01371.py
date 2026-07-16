"""Tests for catalog_01371."""

import pytest

from cartservice.generated.catalog_01371 import (
    Product_01371,
    bucket_by_tag_01371,
    is_valid_sku_01371,
    price_with_tax_01371,
)


def test_price_with_tax_01371():
    assert price_with_tax_01371(1000, 500) == 1050


def test_price_with_tax_negative_01371():
    with pytest.raises(ValueError):
        price_with_tax_01371(1000, -1)


def test_is_valid_sku_01371():
    assert is_valid_sku_01371("abc123")
    assert not is_valid_sku_01371("")


def test_bucket_by_tag_01371():
    p = Product_01371("s1", 100, ["a"])
    assert bucket_by_tag_01371([p]) == {"a": ["s1"]}
