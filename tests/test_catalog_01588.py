"""Tests for catalog_01588."""

import pytest

from cartservice.generated.catalog_01588 import (
    Product_01588,
    bucket_by_tag_01588,
    is_valid_sku_01588,
    price_with_tax_01588,
)


def test_price_with_tax_01588():
    assert price_with_tax_01588(1000, 500) == 1050


def test_price_with_tax_negative_01588():
    with pytest.raises(ValueError):
        price_with_tax_01588(1000, -1)


def test_is_valid_sku_01588():
    assert is_valid_sku_01588("abc123")
    assert not is_valid_sku_01588("")


def test_bucket_by_tag_01588():
    p = Product_01588("s1", 100, ["a"])
    assert bucket_by_tag_01588([p]) == {"a": ["s1"]}
