"""Tests for catalog_00623."""

import pytest

from cartservice.generated.catalog_00623 import (
    Product_00623,
    bucket_by_tag_00623,
    is_valid_sku_00623,
    price_with_tax_00623,
)


def test_price_with_tax_00623():
    assert price_with_tax_00623(1000, 500) == 1050


def test_price_with_tax_negative_00623():
    with pytest.raises(ValueError):
        price_with_tax_00623(1000, -1)


def test_is_valid_sku_00623():
    assert is_valid_sku_00623("abc123")
    assert not is_valid_sku_00623("")


def test_bucket_by_tag_00623():
    p = Product_00623("s1", 100, ["a"])
    assert bucket_by_tag_00623([p]) == {"a": ["s1"]}
