"""Tests for catalog_01273."""

import pytest

from cartservice.generated.catalog_01273 import (
    Product_01273,
    bucket_by_tag_01273,
    is_valid_sku_01273,
    price_with_tax_01273,
)


def test_price_with_tax_01273():
    assert price_with_tax_01273(1000, 500) == 1050


def test_price_with_tax_negative_01273():
    with pytest.raises(ValueError):
        price_with_tax_01273(1000, -1)


def test_is_valid_sku_01273():
    assert is_valid_sku_01273("abc123")
    assert not is_valid_sku_01273("")


def test_bucket_by_tag_01273():
    p = Product_01273("s1", 100, ["a"])
    assert bucket_by_tag_01273([p]) == {"a": ["s1"]}
