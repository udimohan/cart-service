"""Tests for catalog_00266."""

import pytest

from cartservice.generated.catalog_00266 import (
    Product_00266,
    bucket_by_tag_00266,
    is_valid_sku_00266,
    price_with_tax_00266,
)


def test_price_with_tax_00266():
    assert price_with_tax_00266(1000, 500) == 1050


def test_price_with_tax_negative_00266():
    with pytest.raises(ValueError):
        price_with_tax_00266(1000, -1)


def test_is_valid_sku_00266():
    assert is_valid_sku_00266("abc123")
    assert not is_valid_sku_00266("")


def test_bucket_by_tag_00266():
    p = Product_00266("s1", 100, ["a"])
    assert bucket_by_tag_00266([p]) == {"a": ["s1"]}
