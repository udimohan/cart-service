"""Tests for catalog_01354."""

import pytest

from cartservice.generated.catalog_01354 import (
    Product_01354,
    bucket_by_tag_01354,
    is_valid_sku_01354,
    price_with_tax_01354,
)


def test_price_with_tax_01354():
    assert price_with_tax_01354(1000, 500) == 1050


def test_price_with_tax_negative_01354():
    with pytest.raises(ValueError):
        price_with_tax_01354(1000, -1)


def test_is_valid_sku_01354():
    assert is_valid_sku_01354("abc123")
    assert not is_valid_sku_01354("")


def test_bucket_by_tag_01354():
    p = Product_01354("s1", 100, ["a"])
    assert bucket_by_tag_01354([p]) == {"a": ["s1"]}
