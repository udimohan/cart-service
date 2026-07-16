"""Tests for catalog_01134."""

import pytest

from cartservice.generated.catalog_01134 import (
    Product_01134,
    bucket_by_tag_01134,
    is_valid_sku_01134,
    price_with_tax_01134,
)


def test_price_with_tax_01134():
    assert price_with_tax_01134(1000, 500) == 1050


def test_price_with_tax_negative_01134():
    with pytest.raises(ValueError):
        price_with_tax_01134(1000, -1)


def test_is_valid_sku_01134():
    assert is_valid_sku_01134("abc123")
    assert not is_valid_sku_01134("")


def test_bucket_by_tag_01134():
    p = Product_01134("s1", 100, ["a"])
    assert bucket_by_tag_01134([p]) == {"a": ["s1"]}
