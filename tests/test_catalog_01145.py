"""Tests for catalog_01145."""

import pytest

from cartservice.generated.catalog_01145 import (
    Product_01145,
    bucket_by_tag_01145,
    is_valid_sku_01145,
    price_with_tax_01145,
)


def test_price_with_tax_01145():
    assert price_with_tax_01145(1000, 500) == 1050


def test_price_with_tax_negative_01145():
    with pytest.raises(ValueError):
        price_with_tax_01145(1000, -1)


def test_is_valid_sku_01145():
    assert is_valid_sku_01145("abc123")
    assert not is_valid_sku_01145("")


def test_bucket_by_tag_01145():
    p = Product_01145("s1", 100, ["a"])
    assert bucket_by_tag_01145([p]) == {"a": ["s1"]}
