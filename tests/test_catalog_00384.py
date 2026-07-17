"""Tests for catalog_00384."""

import pytest

from cartservice.generated.catalog_00384 import (
    Product_00384,
    bucket_by_tag_00384,
    is_valid_sku_00384,
    price_with_tax_00384,
)


def test_price_with_tax_00384():
    assert price_with_tax_00384(1000, 500) == 1050


def test_price_with_tax_negative_00384():
    with pytest.raises(ValueError):
        price_with_tax_00384(1000, -1)


def test_is_valid_sku_00384():
    assert is_valid_sku_00384("abc123")
    assert not is_valid_sku_00384("")


def test_bucket_by_tag_00384():
    p = Product_00384("s1", 100, ["a"])
    assert bucket_by_tag_00384([p]) == {"a": ["s1"]}
