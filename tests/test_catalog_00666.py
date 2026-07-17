"""Tests for catalog_00666."""

import pytest

from cartservice.generated.catalog_00666 import (
    Product_00666,
    bucket_by_tag_00666,
    is_valid_sku_00666,
    price_with_tax_00666,
)


def test_price_with_tax_00666():
    assert price_with_tax_00666(1000, 500) == 1050


def test_price_with_tax_negative_00666():
    with pytest.raises(ValueError):
        price_with_tax_00666(1000, -1)


def test_is_valid_sku_00666():
    assert is_valid_sku_00666("abc123")
    assert not is_valid_sku_00666("")


def test_bucket_by_tag_00666():
    p = Product_00666("s1", 100, ["a"])
    assert bucket_by_tag_00666([p]) == {"a": ["s1"]}
