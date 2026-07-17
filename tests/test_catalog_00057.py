"""Tests for catalog_00057."""

import pytest

from cartservice.generated.catalog_00057 import (
    Product_00057,
    bucket_by_tag_00057,
    is_valid_sku_00057,
    price_with_tax_00057,
)


def test_price_with_tax_00057():
    assert price_with_tax_00057(1000, 500) == 1050


def test_price_with_tax_negative_00057():
    with pytest.raises(ValueError):
        price_with_tax_00057(1000, -1)


def test_is_valid_sku_00057():
    assert is_valid_sku_00057("abc123")
    assert not is_valid_sku_00057("")


def test_bucket_by_tag_00057():
    p = Product_00057("s1", 100, ["a"])
    assert bucket_by_tag_00057([p]) == {"a": ["s1"]}
