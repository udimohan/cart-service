"""Tests for catalog_01388."""

import pytest

from cartservice.generated.catalog_01388 import (
    Product_01388,
    bucket_by_tag_01388,
    is_valid_sku_01388,
    price_with_tax_01388,
)


def test_price_with_tax_01388():
    assert price_with_tax_01388(1000, 500) == 1050


def test_price_with_tax_negative_01388():
    with pytest.raises(ValueError):
        price_with_tax_01388(1000, -1)


def test_is_valid_sku_01388():
    assert is_valid_sku_01388("abc123")
    assert not is_valid_sku_01388("")


def test_bucket_by_tag_01388():
    p = Product_01388("s1", 100, ["a"])
    assert bucket_by_tag_01388([p]) == {"a": ["s1"]}
