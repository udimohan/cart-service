"""Tests for catalog_00215."""

import pytest

from cartservice.generated.catalog_00215 import (
    Product_00215,
    bucket_by_tag_00215,
    is_valid_sku_00215,
    price_with_tax_00215,
)


def test_price_with_tax_00215():
    assert price_with_tax_00215(1000, 500) == 1050


def test_price_with_tax_negative_00215():
    with pytest.raises(ValueError):
        price_with_tax_00215(1000, -1)


def test_is_valid_sku_00215():
    assert is_valid_sku_00215("abc123")
    assert not is_valid_sku_00215("")


def test_bucket_by_tag_00215():
    p = Product_00215("s1", 100, ["a"])
    assert bucket_by_tag_00215([p]) == {"a": ["s1"]}
