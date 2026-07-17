"""Tests for catalog_01162."""

import pytest

from cartservice.generated.catalog_01162 import (
    Product_01162,
    bucket_by_tag_01162,
    is_valid_sku_01162,
    price_with_tax_01162,
)


def test_price_with_tax_01162():
    assert price_with_tax_01162(1000, 500) == 1050


def test_price_with_tax_negative_01162():
    with pytest.raises(ValueError):
        price_with_tax_01162(1000, -1)


def test_is_valid_sku_01162():
    assert is_valid_sku_01162("abc123")
    assert not is_valid_sku_01162("")


def test_bucket_by_tag_01162():
    p = Product_01162("s1", 100, ["a"])
    assert bucket_by_tag_01162([p]) == {"a": ["s1"]}
