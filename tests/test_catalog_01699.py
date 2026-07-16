"""Tests for catalog_01699."""

import pytest

from cartservice.generated.catalog_01699 import (
    Product_01699,
    bucket_by_tag_01699,
    is_valid_sku_01699,
    price_with_tax_01699,
)


def test_price_with_tax_01699():
    assert price_with_tax_01699(1000, 500) == 1050


def test_price_with_tax_negative_01699():
    with pytest.raises(ValueError):
        price_with_tax_01699(1000, -1)


def test_is_valid_sku_01699():
    assert is_valid_sku_01699("abc123")
    assert not is_valid_sku_01699("")


def test_bucket_by_tag_01699():
    p = Product_01699("s1", 100, ["a"])
    assert bucket_by_tag_01699([p]) == {"a": ["s1"]}
