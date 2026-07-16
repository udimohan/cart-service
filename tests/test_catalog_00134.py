"""Tests for catalog_00134."""

import pytest

from cartservice.generated.catalog_00134 import (
    Product_00134,
    bucket_by_tag_00134,
    is_valid_sku_00134,
    price_with_tax_00134,
)


def test_price_with_tax_00134():
    assert price_with_tax_00134(1000, 500) == 1050


def test_price_with_tax_negative_00134():
    with pytest.raises(ValueError):
        price_with_tax_00134(1000, -1)


def test_is_valid_sku_00134():
    assert is_valid_sku_00134("abc123")
    assert not is_valid_sku_00134("")


def test_bucket_by_tag_00134():
    p = Product_00134("s1", 100, ["a"])
    assert bucket_by_tag_00134([p]) == {"a": ["s1"]}
