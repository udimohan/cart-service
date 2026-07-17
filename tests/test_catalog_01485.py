"""Tests for catalog_01485."""

import pytest

from cartservice.generated.catalog_01485 import (
    Product_01485,
    bucket_by_tag_01485,
    is_valid_sku_01485,
    price_with_tax_01485,
)


def test_price_with_tax_01485():
    assert price_with_tax_01485(1000, 500) == 1050


def test_price_with_tax_negative_01485():
    with pytest.raises(ValueError):
        price_with_tax_01485(1000, -1)


def test_is_valid_sku_01485():
    assert is_valid_sku_01485("abc123")
    assert not is_valid_sku_01485("")


def test_bucket_by_tag_01485():
    p = Product_01485("s1", 100, ["a"])
    assert bucket_by_tag_01485([p]) == {"a": ["s1"]}
