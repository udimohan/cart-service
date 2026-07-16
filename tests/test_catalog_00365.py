"""Tests for catalog_00365."""

import pytest

from cartservice.generated.catalog_00365 import (
    Product_00365,
    bucket_by_tag_00365,
    is_valid_sku_00365,
    price_with_tax_00365,
)


def test_price_with_tax_00365():
    assert price_with_tax_00365(1000, 500) == 1050


def test_price_with_tax_negative_00365():
    with pytest.raises(ValueError):
        price_with_tax_00365(1000, -1)


def test_is_valid_sku_00365():
    assert is_valid_sku_00365("abc123")
    assert not is_valid_sku_00365("")


def test_bucket_by_tag_00365():
    p = Product_00365("s1", 100, ["a"])
    assert bucket_by_tag_00365([p]) == {"a": ["s1"]}
