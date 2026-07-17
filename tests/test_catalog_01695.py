"""Tests for catalog_01695."""

import pytest

from cartservice.generated.catalog_01695 import (
    Product_01695,
    bucket_by_tag_01695,
    is_valid_sku_01695,
    price_with_tax_01695,
)


def test_price_with_tax_01695():
    assert price_with_tax_01695(1000, 500) == 1050


def test_price_with_tax_negative_01695():
    with pytest.raises(ValueError):
        price_with_tax_01695(1000, -1)


def test_is_valid_sku_01695():
    assert is_valid_sku_01695("abc123")
    assert not is_valid_sku_01695("")


def test_bucket_by_tag_01695():
    p = Product_01695("s1", 100, ["a"])
    assert bucket_by_tag_01695([p]) == {"a": ["s1"]}
