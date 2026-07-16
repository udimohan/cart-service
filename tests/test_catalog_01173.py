"""Tests for catalog_01173."""

import pytest

from cartservice.generated.catalog_01173 import (
    Product_01173,
    bucket_by_tag_01173,
    is_valid_sku_01173,
    price_with_tax_01173,
)


def test_price_with_tax_01173():
    assert price_with_tax_01173(1000, 500) == 1050


def test_price_with_tax_negative_01173():
    with pytest.raises(ValueError):
        price_with_tax_01173(1000, -1)


def test_is_valid_sku_01173():
    assert is_valid_sku_01173("abc123")
    assert not is_valid_sku_01173("")


def test_bucket_by_tag_01173():
    p = Product_01173("s1", 100, ["a"])
    assert bucket_by_tag_01173([p]) == {"a": ["s1"]}
