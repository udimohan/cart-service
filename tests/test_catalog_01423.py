"""Tests for catalog_01423."""

import pytest

from cartservice.generated.catalog_01423 import (
    Product_01423,
    bucket_by_tag_01423,
    is_valid_sku_01423,
    price_with_tax_01423,
)


def test_price_with_tax_01423():
    assert price_with_tax_01423(1000, 500) == 1050


def test_price_with_tax_negative_01423():
    with pytest.raises(ValueError):
        price_with_tax_01423(1000, -1)


def test_is_valid_sku_01423():
    assert is_valid_sku_01423("abc123")
    assert not is_valid_sku_01423("")


def test_bucket_by_tag_01423():
    p = Product_01423("s1", 100, ["a"])
    assert bucket_by_tag_01423([p]) == {"a": ["s1"]}
