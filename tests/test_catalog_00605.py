"""Tests for catalog_00605."""

import pytest

from cartservice.generated.catalog_00605 import (
    Product_00605,
    bucket_by_tag_00605,
    is_valid_sku_00605,
    price_with_tax_00605,
)


def test_price_with_tax_00605():
    assert price_with_tax_00605(1000, 500) == 1050


def test_price_with_tax_negative_00605():
    with pytest.raises(ValueError):
        price_with_tax_00605(1000, -1)


def test_is_valid_sku_00605():
    assert is_valid_sku_00605("abc123")
    assert not is_valid_sku_00605("")


def test_bucket_by_tag_00605():
    p = Product_00605("s1", 100, ["a"])
    assert bucket_by_tag_00605([p]) == {"a": ["s1"]}
