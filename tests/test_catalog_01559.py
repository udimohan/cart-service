"""Tests for catalog_01559."""

import pytest

from cartservice.generated.catalog_01559 import (
    Product_01559,
    bucket_by_tag_01559,
    is_valid_sku_01559,
    price_with_tax_01559,
)


def test_price_with_tax_01559():
    assert price_with_tax_01559(1000, 500) == 1050


def test_price_with_tax_negative_01559():
    with pytest.raises(ValueError):
        price_with_tax_01559(1000, -1)


def test_is_valid_sku_01559():
    assert is_valid_sku_01559("abc123")
    assert not is_valid_sku_01559("")


def test_bucket_by_tag_01559():
    p = Product_01559("s1", 100, ["a"])
    assert bucket_by_tag_01559([p]) == {"a": ["s1"]}
