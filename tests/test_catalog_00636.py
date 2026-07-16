"""Tests for catalog_00636."""

import pytest

from cartservice.generated.catalog_00636 import (
    Product_00636,
    bucket_by_tag_00636,
    is_valid_sku_00636,
    price_with_tax_00636,
)


def test_price_with_tax_00636():
    assert price_with_tax_00636(1000, 500) == 1050


def test_price_with_tax_negative_00636():
    with pytest.raises(ValueError):
        price_with_tax_00636(1000, -1)


def test_is_valid_sku_00636():
    assert is_valid_sku_00636("abc123")
    assert not is_valid_sku_00636("")


def test_bucket_by_tag_00636():
    p = Product_00636("s1", 100, ["a"])
    assert bucket_by_tag_00636([p]) == {"a": ["s1"]}
