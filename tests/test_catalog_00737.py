"""Tests for catalog_00737."""

import pytest

from cartservice.generated.catalog_00737 import (
    Product_00737,
    bucket_by_tag_00737,
    is_valid_sku_00737,
    price_with_tax_00737,
)


def test_price_with_tax_00737():
    assert price_with_tax_00737(1000, 500) == 1050


def test_price_with_tax_negative_00737():
    with pytest.raises(ValueError):
        price_with_tax_00737(1000, -1)


def test_is_valid_sku_00737():
    assert is_valid_sku_00737("abc123")
    assert not is_valid_sku_00737("")


def test_bucket_by_tag_00737():
    p = Product_00737("s1", 100, ["a"])
    assert bucket_by_tag_00737([p]) == {"a": ["s1"]}
