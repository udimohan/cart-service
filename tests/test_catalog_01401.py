"""Tests for catalog_01401."""

import pytest

from cartservice.generated.catalog_01401 import (
    Product_01401,
    bucket_by_tag_01401,
    is_valid_sku_01401,
    price_with_tax_01401,
)


def test_price_with_tax_01401():
    assert price_with_tax_01401(1000, 500) == 1050


def test_price_with_tax_negative_01401():
    with pytest.raises(ValueError):
        price_with_tax_01401(1000, -1)


def test_is_valid_sku_01401():
    assert is_valid_sku_01401("abc123")
    assert not is_valid_sku_01401("")


def test_bucket_by_tag_01401():
    p = Product_01401("s1", 100, ["a"])
    assert bucket_by_tag_01401([p]) == {"a": ["s1"]}
