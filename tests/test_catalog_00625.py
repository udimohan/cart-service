"""Tests for catalog_00625."""

import pytest

from cartservice.generated.catalog_00625 import (
    Product_00625,
    bucket_by_tag_00625,
    is_valid_sku_00625,
    price_with_tax_00625,
)


def test_price_with_tax_00625():
    assert price_with_tax_00625(1000, 500) == 1050


def test_price_with_tax_negative_00625():
    with pytest.raises(ValueError):
        price_with_tax_00625(1000, -1)


def test_is_valid_sku_00625():
    assert is_valid_sku_00625("abc123")
    assert not is_valid_sku_00625("")


def test_bucket_by_tag_00625():
    p = Product_00625("s1", 100, ["a"])
    assert bucket_by_tag_00625([p]) == {"a": ["s1"]}
