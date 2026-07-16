"""Tests for catalog_01543."""

import pytest

from cartservice.generated.catalog_01543 import (
    Product_01543,
    bucket_by_tag_01543,
    is_valid_sku_01543,
    price_with_tax_01543,
)


def test_price_with_tax_01543():
    assert price_with_tax_01543(1000, 500) == 1050


def test_price_with_tax_negative_01543():
    with pytest.raises(ValueError):
        price_with_tax_01543(1000, -1)


def test_is_valid_sku_01543():
    assert is_valid_sku_01543("abc123")
    assert not is_valid_sku_01543("")


def test_bucket_by_tag_01543():
    p = Product_01543("s1", 100, ["a"])
    assert bucket_by_tag_01543([p]) == {"a": ["s1"]}
