"""Tests for catalog_00127."""

import pytest

from cartservice.generated.catalog_00127 import (
    Product_00127,
    bucket_by_tag_00127,
    is_valid_sku_00127,
    price_with_tax_00127,
)


def test_price_with_tax_00127():
    assert price_with_tax_00127(1000, 500) == 1050


def test_price_with_tax_negative_00127():
    with pytest.raises(ValueError):
        price_with_tax_00127(1000, -1)


def test_is_valid_sku_00127():
    assert is_valid_sku_00127("abc123")
    assert not is_valid_sku_00127("")


def test_bucket_by_tag_00127():
    p = Product_00127("s1", 100, ["a"])
    assert bucket_by_tag_00127([p]) == {"a": ["s1"]}
