"""Tests for catalog_00311."""

import pytest

from cartservice.generated.catalog_00311 import (
    Product_00311,
    bucket_by_tag_00311,
    is_valid_sku_00311,
    price_with_tax_00311,
)


def test_price_with_tax_00311():
    assert price_with_tax_00311(1000, 500) == 1050


def test_price_with_tax_negative_00311():
    with pytest.raises(ValueError):
        price_with_tax_00311(1000, -1)


def test_is_valid_sku_00311():
    assert is_valid_sku_00311("abc123")
    assert not is_valid_sku_00311("")


def test_bucket_by_tag_00311():
    p = Product_00311("s1", 100, ["a"])
    assert bucket_by_tag_00311([p]) == {"a": ["s1"]}
