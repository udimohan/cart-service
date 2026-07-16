"""Tests for catalog_00961."""

import pytest

from cartservice.generated.catalog_00961 import (
    Product_00961,
    bucket_by_tag_00961,
    is_valid_sku_00961,
    price_with_tax_00961,
)


def test_price_with_tax_00961():
    assert price_with_tax_00961(1000, 500) == 1050


def test_price_with_tax_negative_00961():
    with pytest.raises(ValueError):
        price_with_tax_00961(1000, -1)


def test_is_valid_sku_00961():
    assert is_valid_sku_00961("abc123")
    assert not is_valid_sku_00961("")


def test_bucket_by_tag_00961():
    p = Product_00961("s1", 100, ["a"])
    assert bucket_by_tag_00961([p]) == {"a": ["s1"]}
