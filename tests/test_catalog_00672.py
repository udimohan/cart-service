"""Tests for catalog_00672."""

import pytest

from cartservice.generated.catalog_00672 import (
    Product_00672,
    bucket_by_tag_00672,
    is_valid_sku_00672,
    price_with_tax_00672,
)


def test_price_with_tax_00672():
    assert price_with_tax_00672(1000, 500) == 1050


def test_price_with_tax_negative_00672():
    with pytest.raises(ValueError):
        price_with_tax_00672(1000, -1)


def test_is_valid_sku_00672():
    assert is_valid_sku_00672("abc123")
    assert not is_valid_sku_00672("")


def test_bucket_by_tag_00672():
    p = Product_00672("s1", 100, ["a"])
    assert bucket_by_tag_00672([p]) == {"a": ["s1"]}
