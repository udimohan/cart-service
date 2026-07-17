"""Tests for catalog_00382."""

import pytest

from cartservice.generated.catalog_00382 import (
    Product_00382,
    bucket_by_tag_00382,
    is_valid_sku_00382,
    price_with_tax_00382,
)


def test_price_with_tax_00382():
    assert price_with_tax_00382(1000, 500) == 1050


def test_price_with_tax_negative_00382():
    with pytest.raises(ValueError):
        price_with_tax_00382(1000, -1)


def test_is_valid_sku_00382():
    assert is_valid_sku_00382("abc123")
    assert not is_valid_sku_00382("")


def test_bucket_by_tag_00382():
    p = Product_00382("s1", 100, ["a"])
    assert bucket_by_tag_00382([p]) == {"a": ["s1"]}
