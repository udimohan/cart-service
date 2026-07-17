"""Tests for catalog_01365."""

import pytest

from cartservice.generated.catalog_01365 import (
    Product_01365,
    bucket_by_tag_01365,
    is_valid_sku_01365,
    price_with_tax_01365,
)


def test_price_with_tax_01365():
    assert price_with_tax_01365(1000, 500) == 1050


def test_price_with_tax_negative_01365():
    with pytest.raises(ValueError):
        price_with_tax_01365(1000, -1)


def test_is_valid_sku_01365():
    assert is_valid_sku_01365("abc123")
    assert not is_valid_sku_01365("")


def test_bucket_by_tag_01365():
    p = Product_01365("s1", 100, ["a"])
    assert bucket_by_tag_01365([p]) == {"a": ["s1"]}
