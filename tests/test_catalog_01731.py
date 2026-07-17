"""Tests for catalog_01731."""

import pytest

from cartservice.generated.catalog_01731 import (
    Product_01731,
    bucket_by_tag_01731,
    is_valid_sku_01731,
    price_with_tax_01731,
)


def test_price_with_tax_01731():
    assert price_with_tax_01731(1000, 500) == 1050


def test_price_with_tax_negative_01731():
    with pytest.raises(ValueError):
        price_with_tax_01731(1000, -1)


def test_is_valid_sku_01731():
    assert is_valid_sku_01731("abc123")
    assert not is_valid_sku_01731("")


def test_bucket_by_tag_01731():
    p = Product_01731("s1", 100, ["a"])
    assert bucket_by_tag_01731([p]) == {"a": ["s1"]}
