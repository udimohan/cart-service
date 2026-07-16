"""Tests for catalog_01652."""

import pytest

from cartservice.generated.catalog_01652 import (
    Product_01652,
    bucket_by_tag_01652,
    is_valid_sku_01652,
    price_with_tax_01652,
)


def test_price_with_tax_01652():
    assert price_with_tax_01652(1000, 500) == 1050


def test_price_with_tax_negative_01652():
    with pytest.raises(ValueError):
        price_with_tax_01652(1000, -1)


def test_is_valid_sku_01652():
    assert is_valid_sku_01652("abc123")
    assert not is_valid_sku_01652("")


def test_bucket_by_tag_01652():
    p = Product_01652("s1", 100, ["a"])
    assert bucket_by_tag_01652([p]) == {"a": ["s1"]}
