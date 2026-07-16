"""Tests for catalog_01215."""

import pytest

from cartservice.generated.catalog_01215 import (
    Product_01215,
    bucket_by_tag_01215,
    is_valid_sku_01215,
    price_with_tax_01215,
)


def test_price_with_tax_01215():
    assert price_with_tax_01215(1000, 500) == 1050


def test_price_with_tax_negative_01215():
    with pytest.raises(ValueError):
        price_with_tax_01215(1000, -1)


def test_is_valid_sku_01215():
    assert is_valid_sku_01215("abc123")
    assert not is_valid_sku_01215("")


def test_bucket_by_tag_01215():
    p = Product_01215("s1", 100, ["a"])
    assert bucket_by_tag_01215([p]) == {"a": ["s1"]}
