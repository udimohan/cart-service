"""Tests for catalog_01706."""

import pytest

from cartservice.generated.catalog_01706 import (
    Product_01706,
    bucket_by_tag_01706,
    is_valid_sku_01706,
    price_with_tax_01706,
)


def test_price_with_tax_01706():
    assert price_with_tax_01706(1000, 500) == 1050


def test_price_with_tax_negative_01706():
    with pytest.raises(ValueError):
        price_with_tax_01706(1000, -1)


def test_is_valid_sku_01706():
    assert is_valid_sku_01706("abc123")
    assert not is_valid_sku_01706("")


def test_bucket_by_tag_01706():
    p = Product_01706("s1", 100, ["a"])
    assert bucket_by_tag_01706([p]) == {"a": ["s1"]}
