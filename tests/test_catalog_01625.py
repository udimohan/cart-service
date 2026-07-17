"""Tests for catalog_01625."""

import pytest

from cartservice.generated.catalog_01625 import (
    Product_01625,
    bucket_by_tag_01625,
    is_valid_sku_01625,
    price_with_tax_01625,
)


def test_price_with_tax_01625():
    assert price_with_tax_01625(1000, 500) == 1050


def test_price_with_tax_negative_01625():
    with pytest.raises(ValueError):
        price_with_tax_01625(1000, -1)


def test_is_valid_sku_01625():
    assert is_valid_sku_01625("abc123")
    assert not is_valid_sku_01625("")


def test_bucket_by_tag_01625():
    p = Product_01625("s1", 100, ["a"])
    assert bucket_by_tag_01625([p]) == {"a": ["s1"]}
