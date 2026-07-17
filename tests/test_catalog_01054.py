"""Tests for catalog_01054."""

import pytest

from cartservice.generated.catalog_01054 import (
    Product_01054,
    bucket_by_tag_01054,
    is_valid_sku_01054,
    price_with_tax_01054,
)


def test_price_with_tax_01054():
    assert price_with_tax_01054(1000, 500) == 1050


def test_price_with_tax_negative_01054():
    with pytest.raises(ValueError):
        price_with_tax_01054(1000, -1)


def test_is_valid_sku_01054():
    assert is_valid_sku_01054("abc123")
    assert not is_valid_sku_01054("")


def test_bucket_by_tag_01054():
    p = Product_01054("s1", 100, ["a"])
    assert bucket_by_tag_01054([p]) == {"a": ["s1"]}
