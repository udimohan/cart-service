"""Tests for catalog_01697."""

import pytest

from cartservice.generated.catalog_01697 import (
    Product_01697,
    bucket_by_tag_01697,
    is_valid_sku_01697,
    price_with_tax_01697,
)


def test_price_with_tax_01697():
    assert price_with_tax_01697(1000, 500) == 1050


def test_price_with_tax_negative_01697():
    with pytest.raises(ValueError):
        price_with_tax_01697(1000, -1)


def test_is_valid_sku_01697():
    assert is_valid_sku_01697("abc123")
    assert not is_valid_sku_01697("")


def test_bucket_by_tag_01697():
    p = Product_01697("s1", 100, ["a"])
    assert bucket_by_tag_01697([p]) == {"a": ["s1"]}
