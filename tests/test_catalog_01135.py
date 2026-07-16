"""Tests for catalog_01135."""

import pytest

from cartservice.generated.catalog_01135 import (
    Product_01135,
    bucket_by_tag_01135,
    is_valid_sku_01135,
    price_with_tax_01135,
)


def test_price_with_tax_01135():
    assert price_with_tax_01135(1000, 500) == 1050


def test_price_with_tax_negative_01135():
    with pytest.raises(ValueError):
        price_with_tax_01135(1000, -1)


def test_is_valid_sku_01135():
    assert is_valid_sku_01135("abc123")
    assert not is_valid_sku_01135("")


def test_bucket_by_tag_01135():
    p = Product_01135("s1", 100, ["a"])
    assert bucket_by_tag_01135([p]) == {"a": ["s1"]}
