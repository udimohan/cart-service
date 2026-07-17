"""Tests for catalog_00135."""

import pytest

from cartservice.generated.catalog_00135 import (
    Product_00135,
    bucket_by_tag_00135,
    is_valid_sku_00135,
    price_with_tax_00135,
)


def test_price_with_tax_00135():
    assert price_with_tax_00135(1000, 500) == 1050


def test_price_with_tax_negative_00135():
    with pytest.raises(ValueError):
        price_with_tax_00135(1000, -1)


def test_is_valid_sku_00135():
    assert is_valid_sku_00135("abc123")
    assert not is_valid_sku_00135("")


def test_bucket_by_tag_00135():
    p = Product_00135("s1", 100, ["a"])
    assert bucket_by_tag_00135([p]) == {"a": ["s1"]}
