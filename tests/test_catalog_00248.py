"""Tests for catalog_00248."""

import pytest

from cartservice.generated.catalog_00248 import (
    Product_00248,
    bucket_by_tag_00248,
    is_valid_sku_00248,
    price_with_tax_00248,
)


def test_price_with_tax_00248():
    assert price_with_tax_00248(1000, 500) == 1050


def test_price_with_tax_negative_00248():
    with pytest.raises(ValueError):
        price_with_tax_00248(1000, -1)


def test_is_valid_sku_00248():
    assert is_valid_sku_00248("abc123")
    assert not is_valid_sku_00248("")


def test_bucket_by_tag_00248():
    p = Product_00248("s1", 100, ["a"])
    assert bucket_by_tag_00248([p]) == {"a": ["s1"]}
