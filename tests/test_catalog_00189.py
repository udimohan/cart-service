"""Tests for catalog_00189."""

import pytest

from cartservice.generated.catalog_00189 import (
    Product_00189,
    bucket_by_tag_00189,
    is_valid_sku_00189,
    price_with_tax_00189,
)


def test_price_with_tax_00189():
    assert price_with_tax_00189(1000, 500) == 1050


def test_price_with_tax_negative_00189():
    with pytest.raises(ValueError):
        price_with_tax_00189(1000, -1)


def test_is_valid_sku_00189():
    assert is_valid_sku_00189("abc123")
    assert not is_valid_sku_00189("")


def test_bucket_by_tag_00189():
    p = Product_00189("s1", 100, ["a"])
    assert bucket_by_tag_00189([p]) == {"a": ["s1"]}
