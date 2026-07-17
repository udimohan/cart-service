"""Tests for catalog_01061."""

import pytest

from cartservice.generated.catalog_01061 import (
    Product_01061,
    bucket_by_tag_01061,
    is_valid_sku_01061,
    price_with_tax_01061,
)


def test_price_with_tax_01061():
    assert price_with_tax_01061(1000, 500) == 1050


def test_price_with_tax_negative_01061():
    with pytest.raises(ValueError):
        price_with_tax_01061(1000, -1)


def test_is_valid_sku_01061():
    assert is_valid_sku_01061("abc123")
    assert not is_valid_sku_01061("")


def test_bucket_by_tag_01061():
    p = Product_01061("s1", 100, ["a"])
    assert bucket_by_tag_01061([p]) == {"a": ["s1"]}
