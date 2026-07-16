"""Tests for catalog_01346."""

import pytest

from cartservice.generated.catalog_01346 import (
    Product_01346,
    bucket_by_tag_01346,
    is_valid_sku_01346,
    price_with_tax_01346,
)


def test_price_with_tax_01346():
    assert price_with_tax_01346(1000, 500) == 1050


def test_price_with_tax_negative_01346():
    with pytest.raises(ValueError):
        price_with_tax_01346(1000, -1)


def test_is_valid_sku_01346():
    assert is_valid_sku_01346("abc123")
    assert not is_valid_sku_01346("")


def test_bucket_by_tag_01346():
    p = Product_01346("s1", 100, ["a"])
    assert bucket_by_tag_01346([p]) == {"a": ["s1"]}
