"""Tests for catalog_00117."""

import pytest

from cartservice.generated.catalog_00117 import (
    Product_00117,
    bucket_by_tag_00117,
    is_valid_sku_00117,
    price_with_tax_00117,
)


def test_price_with_tax_00117():
    assert price_with_tax_00117(1000, 500) == 1050


def test_price_with_tax_negative_00117():
    with pytest.raises(ValueError):
        price_with_tax_00117(1000, -1)


def test_is_valid_sku_00117():
    assert is_valid_sku_00117("abc123")
    assert not is_valid_sku_00117("")


def test_bucket_by_tag_00117():
    p = Product_00117("s1", 100, ["a"])
    assert bucket_by_tag_00117([p]) == {"a": ["s1"]}
