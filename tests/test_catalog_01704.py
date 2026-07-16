"""Tests for catalog_01704."""

import pytest

from cartservice.generated.catalog_01704 import (
    Product_01704,
    bucket_by_tag_01704,
    is_valid_sku_01704,
    price_with_tax_01704,
)


def test_price_with_tax_01704():
    assert price_with_tax_01704(1000, 500) == 1050


def test_price_with_tax_negative_01704():
    with pytest.raises(ValueError):
        price_with_tax_01704(1000, -1)


def test_is_valid_sku_01704():
    assert is_valid_sku_01704("abc123")
    assert not is_valid_sku_01704("")


def test_bucket_by_tag_01704():
    p = Product_01704("s1", 100, ["a"])
    assert bucket_by_tag_01704([p]) == {"a": ["s1"]}
