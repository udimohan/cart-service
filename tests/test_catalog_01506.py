"""Tests for catalog_01506."""

import pytest

from cartservice.generated.catalog_01506 import (
    Product_01506,
    bucket_by_tag_01506,
    is_valid_sku_01506,
    price_with_tax_01506,
)


def test_price_with_tax_01506():
    assert price_with_tax_01506(1000, 500) == 1050


def test_price_with_tax_negative_01506():
    with pytest.raises(ValueError):
        price_with_tax_01506(1000, -1)


def test_is_valid_sku_01506():
    assert is_valid_sku_01506("abc123")
    assert not is_valid_sku_01506("")


def test_bucket_by_tag_01506():
    p = Product_01506("s1", 100, ["a"])
    assert bucket_by_tag_01506([p]) == {"a": ["s1"]}
