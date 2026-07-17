"""Tests for catalog_00617."""

import pytest

from cartservice.generated.catalog_00617 import (
    Product_00617,
    bucket_by_tag_00617,
    is_valid_sku_00617,
    price_with_tax_00617,
)


def test_price_with_tax_00617():
    assert price_with_tax_00617(1000, 500) == 1050


def test_price_with_tax_negative_00617():
    with pytest.raises(ValueError):
        price_with_tax_00617(1000, -1)


def test_is_valid_sku_00617():
    assert is_valid_sku_00617("abc123")
    assert not is_valid_sku_00617("")


def test_bucket_by_tag_00617():
    p = Product_00617("s1", 100, ["a"])
    assert bucket_by_tag_00617([p]) == {"a": ["s1"]}
