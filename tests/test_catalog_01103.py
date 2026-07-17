"""Tests for catalog_01103."""

import pytest

from cartservice.generated.catalog_01103 import (
    Product_01103,
    bucket_by_tag_01103,
    is_valid_sku_01103,
    price_with_tax_01103,
)


def test_price_with_tax_01103():
    assert price_with_tax_01103(1000, 500) == 1050


def test_price_with_tax_negative_01103():
    with pytest.raises(ValueError):
        price_with_tax_01103(1000, -1)


def test_is_valid_sku_01103():
    assert is_valid_sku_01103("abc123")
    assert not is_valid_sku_01103("")


def test_bucket_by_tag_01103():
    p = Product_01103("s1", 100, ["a"])
    assert bucket_by_tag_01103([p]) == {"a": ["s1"]}
