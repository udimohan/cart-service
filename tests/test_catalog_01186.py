"""Tests for catalog_01186."""

import pytest

from cartservice.generated.catalog_01186 import (
    Product_01186,
    bucket_by_tag_01186,
    is_valid_sku_01186,
    price_with_tax_01186,
)


def test_price_with_tax_01186():
    assert price_with_tax_01186(1000, 500) == 1050


def test_price_with_tax_negative_01186():
    with pytest.raises(ValueError):
        price_with_tax_01186(1000, -1)


def test_is_valid_sku_01186():
    assert is_valid_sku_01186("abc123")
    assert not is_valid_sku_01186("")


def test_bucket_by_tag_01186():
    p = Product_01186("s1", 100, ["a"])
    assert bucket_by_tag_01186([p]) == {"a": ["s1"]}
