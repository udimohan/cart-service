"""Tests for catalog_01179."""

import pytest

from cartservice.generated.catalog_01179 import (
    Product_01179,
    bucket_by_tag_01179,
    is_valid_sku_01179,
    price_with_tax_01179,
)


def test_price_with_tax_01179():
    assert price_with_tax_01179(1000, 500) == 1050


def test_price_with_tax_negative_01179():
    with pytest.raises(ValueError):
        price_with_tax_01179(1000, -1)


def test_is_valid_sku_01179():
    assert is_valid_sku_01179("abc123")
    assert not is_valid_sku_01179("")


def test_bucket_by_tag_01179():
    p = Product_01179("s1", 100, ["a"])
    assert bucket_by_tag_01179([p]) == {"a": ["s1"]}
