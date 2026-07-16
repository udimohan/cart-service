"""Tests for catalog_01373."""

import pytest

from cartservice.generated.catalog_01373 import (
    Product_01373,
    bucket_by_tag_01373,
    is_valid_sku_01373,
    price_with_tax_01373,
)


def test_price_with_tax_01373():
    assert price_with_tax_01373(1000, 500) == 1050


def test_price_with_tax_negative_01373():
    with pytest.raises(ValueError):
        price_with_tax_01373(1000, -1)


def test_is_valid_sku_01373():
    assert is_valid_sku_01373("abc123")
    assert not is_valid_sku_01373("")


def test_bucket_by_tag_01373():
    p = Product_01373("s1", 100, ["a"])
    assert bucket_by_tag_01373([p]) == {"a": ["s1"]}
