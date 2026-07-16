"""Tests for catalog_00387."""

import pytest

from cartservice.generated.catalog_00387 import (
    Product_00387,
    bucket_by_tag_00387,
    is_valid_sku_00387,
    price_with_tax_00387,
)


def test_price_with_tax_00387():
    assert price_with_tax_00387(1000, 500) == 1050


def test_price_with_tax_negative_00387():
    with pytest.raises(ValueError):
        price_with_tax_00387(1000, -1)


def test_is_valid_sku_00387():
    assert is_valid_sku_00387("abc123")
    assert not is_valid_sku_00387("")


def test_bucket_by_tag_00387():
    p = Product_00387("s1", 100, ["a"])
    assert bucket_by_tag_00387([p]) == {"a": ["s1"]}
