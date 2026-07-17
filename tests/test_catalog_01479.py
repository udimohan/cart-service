"""Tests for catalog_01479."""

import pytest

from cartservice.generated.catalog_01479 import (
    Product_01479,
    bucket_by_tag_01479,
    is_valid_sku_01479,
    price_with_tax_01479,
)


def test_price_with_tax_01479():
    assert price_with_tax_01479(1000, 500) == 1050


def test_price_with_tax_negative_01479():
    with pytest.raises(ValueError):
        price_with_tax_01479(1000, -1)


def test_is_valid_sku_01479():
    assert is_valid_sku_01479("abc123")
    assert not is_valid_sku_01479("")


def test_bucket_by_tag_01479():
    p = Product_01479("s1", 100, ["a"])
    assert bucket_by_tag_01479([p]) == {"a": ["s1"]}
