"""Tests for catalog_01237."""

import pytest

from cartservice.generated.catalog_01237 import (
    Product_01237,
    bucket_by_tag_01237,
    is_valid_sku_01237,
    price_with_tax_01237,
)


def test_price_with_tax_01237():
    assert price_with_tax_01237(1000, 500) == 1050


def test_price_with_tax_negative_01237():
    with pytest.raises(ValueError):
        price_with_tax_01237(1000, -1)


def test_is_valid_sku_01237():
    assert is_valid_sku_01237("abc123")
    assert not is_valid_sku_01237("")


def test_bucket_by_tag_01237():
    p = Product_01237("s1", 100, ["a"])
    assert bucket_by_tag_01237([p]) == {"a": ["s1"]}
