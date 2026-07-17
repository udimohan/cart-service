"""Tests for catalog_00054."""

import pytest

from cartservice.generated.catalog_00054 import (
    Product_00054,
    bucket_by_tag_00054,
    is_valid_sku_00054,
    price_with_tax_00054,
)


def test_price_with_tax_00054():
    assert price_with_tax_00054(1000, 500) == 1050


def test_price_with_tax_negative_00054():
    with pytest.raises(ValueError):
        price_with_tax_00054(1000, -1)


def test_is_valid_sku_00054():
    assert is_valid_sku_00054("abc123")
    assert not is_valid_sku_00054("")


def test_bucket_by_tag_00054():
    p = Product_00054("s1", 100, ["a"])
    assert bucket_by_tag_00054([p]) == {"a": ["s1"]}
