"""Tests for catalog_00773."""

import pytest

from cartservice.generated.catalog_00773 import (
    Product_00773,
    bucket_by_tag_00773,
    is_valid_sku_00773,
    price_with_tax_00773,
)


def test_price_with_tax_00773():
    assert price_with_tax_00773(1000, 500) == 1050


def test_price_with_tax_negative_00773():
    with pytest.raises(ValueError):
        price_with_tax_00773(1000, -1)


def test_is_valid_sku_00773():
    assert is_valid_sku_00773("abc123")
    assert not is_valid_sku_00773("")


def test_bucket_by_tag_00773():
    p = Product_00773("s1", 100, ["a"])
    assert bucket_by_tag_00773([p]) == {"a": ["s1"]}
