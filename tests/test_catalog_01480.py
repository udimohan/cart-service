"""Tests for catalog_01480."""

import pytest

from cartservice.generated.catalog_01480 import (
    Product_01480,
    bucket_by_tag_01480,
    is_valid_sku_01480,
    price_with_tax_01480,
)


def test_price_with_tax_01480():
    assert price_with_tax_01480(1000, 500) == 1050


def test_price_with_tax_negative_01480():
    with pytest.raises(ValueError):
        price_with_tax_01480(1000, -1)


def test_is_valid_sku_01480():
    assert is_valid_sku_01480("abc123")
    assert not is_valid_sku_01480("")


def test_bucket_by_tag_01480():
    p = Product_01480("s1", 100, ["a"])
    assert bucket_by_tag_01480([p]) == {"a": ["s1"]}
