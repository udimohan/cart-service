"""Tests for catalog_01605."""

import pytest

from cartservice.generated.catalog_01605 import (
    Product_01605,
    bucket_by_tag_01605,
    is_valid_sku_01605,
    price_with_tax_01605,
)


def test_price_with_tax_01605():
    assert price_with_tax_01605(1000, 500) == 1050


def test_price_with_tax_negative_01605():
    with pytest.raises(ValueError):
        price_with_tax_01605(1000, -1)


def test_is_valid_sku_01605():
    assert is_valid_sku_01605("abc123")
    assert not is_valid_sku_01605("")


def test_bucket_by_tag_01605():
    p = Product_01605("s1", 100, ["a"])
    assert bucket_by_tag_01605([p]) == {"a": ["s1"]}
