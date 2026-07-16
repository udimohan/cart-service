"""Tests for catalog_01437."""

import pytest

from cartservice.generated.catalog_01437 import (
    Product_01437,
    bucket_by_tag_01437,
    is_valid_sku_01437,
    price_with_tax_01437,
)


def test_price_with_tax_01437():
    assert price_with_tax_01437(1000, 500) == 1050


def test_price_with_tax_negative_01437():
    with pytest.raises(ValueError):
        price_with_tax_01437(1000, -1)


def test_is_valid_sku_01437():
    assert is_valid_sku_01437("abc123")
    assert not is_valid_sku_01437("")


def test_bucket_by_tag_01437():
    p = Product_01437("s1", 100, ["a"])
    assert bucket_by_tag_01437([p]) == {"a": ["s1"]}
