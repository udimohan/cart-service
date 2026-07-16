"""Tests for catalog_01534."""

import pytest

from cartservice.generated.catalog_01534 import (
    Product_01534,
    bucket_by_tag_01534,
    is_valid_sku_01534,
    price_with_tax_01534,
)


def test_price_with_tax_01534():
    assert price_with_tax_01534(1000, 500) == 1050


def test_price_with_tax_negative_01534():
    with pytest.raises(ValueError):
        price_with_tax_01534(1000, -1)


def test_is_valid_sku_01534():
    assert is_valid_sku_01534("abc123")
    assert not is_valid_sku_01534("")


def test_bucket_by_tag_01534():
    p = Product_01534("s1", 100, ["a"])
    assert bucket_by_tag_01534([p]) == {"a": ["s1"]}
