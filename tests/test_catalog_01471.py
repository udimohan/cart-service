"""Tests for catalog_01471."""

import pytest

from cartservice.generated.catalog_01471 import (
    Product_01471,
    bucket_by_tag_01471,
    is_valid_sku_01471,
    price_with_tax_01471,
)


def test_price_with_tax_01471():
    assert price_with_tax_01471(1000, 500) == 1050


def test_price_with_tax_negative_01471():
    with pytest.raises(ValueError):
        price_with_tax_01471(1000, -1)


def test_is_valid_sku_01471():
    assert is_valid_sku_01471("abc123")
    assert not is_valid_sku_01471("")


def test_bucket_by_tag_01471():
    p = Product_01471("s1", 100, ["a"])
    assert bucket_by_tag_01471([p]) == {"a": ["s1"]}
