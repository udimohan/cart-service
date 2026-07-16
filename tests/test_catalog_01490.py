"""Tests for catalog_01490."""

import pytest

from cartservice.generated.catalog_01490 import (
    Product_01490,
    bucket_by_tag_01490,
    is_valid_sku_01490,
    price_with_tax_01490,
)


def test_price_with_tax_01490():
    assert price_with_tax_01490(1000, 500) == 1050


def test_price_with_tax_negative_01490():
    with pytest.raises(ValueError):
        price_with_tax_01490(1000, -1)


def test_is_valid_sku_01490():
    assert is_valid_sku_01490("abc123")
    assert not is_valid_sku_01490("")


def test_bucket_by_tag_01490():
    p = Product_01490("s1", 100, ["a"])
    assert bucket_by_tag_01490([p]) == {"a": ["s1"]}
