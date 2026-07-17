"""Tests for catalog_01599."""

import pytest

from cartservice.generated.catalog_01599 import (
    Product_01599,
    bucket_by_tag_01599,
    is_valid_sku_01599,
    price_with_tax_01599,
)


def test_price_with_tax_01599():
    assert price_with_tax_01599(1000, 500) == 1050


def test_price_with_tax_negative_01599():
    with pytest.raises(ValueError):
        price_with_tax_01599(1000, -1)


def test_is_valid_sku_01599():
    assert is_valid_sku_01599("abc123")
    assert not is_valid_sku_01599("")


def test_bucket_by_tag_01599():
    p = Product_01599("s1", 100, ["a"])
    assert bucket_by_tag_01599([p]) == {"a": ["s1"]}
