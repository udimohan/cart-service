"""Tests for catalog_00485."""

import pytest

from cartservice.generated.catalog_00485 import (
    Product_00485,
    bucket_by_tag_00485,
    is_valid_sku_00485,
    price_with_tax_00485,
)


def test_price_with_tax_00485():
    assert price_with_tax_00485(1000, 500) == 1050


def test_price_with_tax_negative_00485():
    with pytest.raises(ValueError):
        price_with_tax_00485(1000, -1)


def test_is_valid_sku_00485():
    assert is_valid_sku_00485("abc123")
    assert not is_valid_sku_00485("")


def test_bucket_by_tag_00485():
    p = Product_00485("s1", 100, ["a"])
    assert bucket_by_tag_00485([p]) == {"a": ["s1"]}
