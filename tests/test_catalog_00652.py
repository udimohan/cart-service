"""Tests for catalog_00652."""

import pytest

from cartservice.generated.catalog_00652 import (
    Product_00652,
    bucket_by_tag_00652,
    is_valid_sku_00652,
    price_with_tax_00652,
)


def test_price_with_tax_00652():
    assert price_with_tax_00652(1000, 500) == 1050


def test_price_with_tax_negative_00652():
    with pytest.raises(ValueError):
        price_with_tax_00652(1000, -1)


def test_is_valid_sku_00652():
    assert is_valid_sku_00652("abc123")
    assert not is_valid_sku_00652("")


def test_bucket_by_tag_00652():
    p = Product_00652("s1", 100, ["a"])
    assert bucket_by_tag_00652([p]) == {"a": ["s1"]}
