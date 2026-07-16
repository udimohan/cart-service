"""Tests for catalog_01402."""

import pytest

from cartservice.generated.catalog_01402 import (
    Product_01402,
    bucket_by_tag_01402,
    is_valid_sku_01402,
    price_with_tax_01402,
)


def test_price_with_tax_01402():
    assert price_with_tax_01402(1000, 500) == 1050


def test_price_with_tax_negative_01402():
    with pytest.raises(ValueError):
        price_with_tax_01402(1000, -1)


def test_is_valid_sku_01402():
    assert is_valid_sku_01402("abc123")
    assert not is_valid_sku_01402("")


def test_bucket_by_tag_01402():
    p = Product_01402("s1", 100, ["a"])
    assert bucket_by_tag_01402([p]) == {"a": ["s1"]}
