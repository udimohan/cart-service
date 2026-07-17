"""Tests for catalog_01121."""

import pytest

from cartservice.generated.catalog_01121 import (
    Product_01121,
    bucket_by_tag_01121,
    is_valid_sku_01121,
    price_with_tax_01121,
)


def test_price_with_tax_01121():
    assert price_with_tax_01121(1000, 500) == 1050


def test_price_with_tax_negative_01121():
    with pytest.raises(ValueError):
        price_with_tax_01121(1000, -1)


def test_is_valid_sku_01121():
    assert is_valid_sku_01121("abc123")
    assert not is_valid_sku_01121("")


def test_bucket_by_tag_01121():
    p = Product_01121("s1", 100, ["a"])
    assert bucket_by_tag_01121([p]) == {"a": ["s1"]}
