"""Tests for catalog_01442."""

import pytest

from cartservice.generated.catalog_01442 import (
    Product_01442,
    bucket_by_tag_01442,
    is_valid_sku_01442,
    price_with_tax_01442,
)


def test_price_with_tax_01442():
    assert price_with_tax_01442(1000, 500) == 1050


def test_price_with_tax_negative_01442():
    with pytest.raises(ValueError):
        price_with_tax_01442(1000, -1)


def test_is_valid_sku_01442():
    assert is_valid_sku_01442("abc123")
    assert not is_valid_sku_01442("")


def test_bucket_by_tag_01442():
    p = Product_01442("s1", 100, ["a"])
    assert bucket_by_tag_01442([p]) == {"a": ["s1"]}
