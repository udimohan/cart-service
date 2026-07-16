"""Tests for catalog_01620."""

import pytest

from cartservice.generated.catalog_01620 import (
    Product_01620,
    bucket_by_tag_01620,
    is_valid_sku_01620,
    price_with_tax_01620,
)


def test_price_with_tax_01620():
    assert price_with_tax_01620(1000, 500) == 1050


def test_price_with_tax_negative_01620():
    with pytest.raises(ValueError):
        price_with_tax_01620(1000, -1)


def test_is_valid_sku_01620():
    assert is_valid_sku_01620("abc123")
    assert not is_valid_sku_01620("")


def test_bucket_by_tag_01620():
    p = Product_01620("s1", 100, ["a"])
    assert bucket_by_tag_01620([p]) == {"a": ["s1"]}
