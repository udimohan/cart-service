"""Tests for catalog_00689."""

import pytest

from cartservice.generated.catalog_00689 import (
    Product_00689,
    bucket_by_tag_00689,
    is_valid_sku_00689,
    price_with_tax_00689,
)


def test_price_with_tax_00689():
    assert price_with_tax_00689(1000, 500) == 1050


def test_price_with_tax_negative_00689():
    with pytest.raises(ValueError):
        price_with_tax_00689(1000, -1)


def test_is_valid_sku_00689():
    assert is_valid_sku_00689("abc123")
    assert not is_valid_sku_00689("")


def test_bucket_by_tag_00689():
    p = Product_00689("s1", 100, ["a"])
    assert bucket_by_tag_00689([p]) == {"a": ["s1"]}
