"""Tests for catalog_01283."""

import pytest

from cartservice.generated.catalog_01283 import (
    Product_01283,
    bucket_by_tag_01283,
    is_valid_sku_01283,
    price_with_tax_01283,
)


def test_price_with_tax_01283():
    assert price_with_tax_01283(1000, 500) == 1050


def test_price_with_tax_negative_01283():
    with pytest.raises(ValueError):
        price_with_tax_01283(1000, -1)


def test_is_valid_sku_01283():
    assert is_valid_sku_01283("abc123")
    assert not is_valid_sku_01283("")


def test_bucket_by_tag_01283():
    p = Product_01283("s1", 100, ["a"])
    assert bucket_by_tag_01283([p]) == {"a": ["s1"]}
