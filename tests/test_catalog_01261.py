"""Tests for catalog_01261."""

import pytest

from cartservice.generated.catalog_01261 import (
    Product_01261,
    bucket_by_tag_01261,
    is_valid_sku_01261,
    price_with_tax_01261,
)


def test_price_with_tax_01261():
    assert price_with_tax_01261(1000, 500) == 1050


def test_price_with_tax_negative_01261():
    with pytest.raises(ValueError):
        price_with_tax_01261(1000, -1)


def test_is_valid_sku_01261():
    assert is_valid_sku_01261("abc123")
    assert not is_valid_sku_01261("")


def test_bucket_by_tag_01261():
    p = Product_01261("s1", 100, ["a"])
    assert bucket_by_tag_01261([p]) == {"a": ["s1"]}
