"""Tests for catalog_01646."""

import pytest

from cartservice.generated.catalog_01646 import (
    Product_01646,
    bucket_by_tag_01646,
    is_valid_sku_01646,
    price_with_tax_01646,
)


def test_price_with_tax_01646():
    assert price_with_tax_01646(1000, 500) == 1050


def test_price_with_tax_negative_01646():
    with pytest.raises(ValueError):
        price_with_tax_01646(1000, -1)


def test_is_valid_sku_01646():
    assert is_valid_sku_01646("abc123")
    assert not is_valid_sku_01646("")


def test_bucket_by_tag_01646():
    p = Product_01646("s1", 100, ["a"])
    assert bucket_by_tag_01646([p]) == {"a": ["s1"]}
