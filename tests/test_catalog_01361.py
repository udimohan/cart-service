"""Tests for catalog_01361."""

import pytest

from cartservice.generated.catalog_01361 import (
    Product_01361,
    bucket_by_tag_01361,
    is_valid_sku_01361,
    price_with_tax_01361,
)


def test_price_with_tax_01361():
    assert price_with_tax_01361(1000, 500) == 1050


def test_price_with_tax_negative_01361():
    with pytest.raises(ValueError):
        price_with_tax_01361(1000, -1)


def test_is_valid_sku_01361():
    assert is_valid_sku_01361("abc123")
    assert not is_valid_sku_01361("")


def test_bucket_by_tag_01361():
    p = Product_01361("s1", 100, ["a"])
    assert bucket_by_tag_01361([p]) == {"a": ["s1"]}
