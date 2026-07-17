"""Tests for catalog_00733."""

import pytest

from cartservice.generated.catalog_00733 import (
    Product_00733,
    bucket_by_tag_00733,
    is_valid_sku_00733,
    price_with_tax_00733,
)


def test_price_with_tax_00733():
    assert price_with_tax_00733(1000, 500) == 1050


def test_price_with_tax_negative_00733():
    with pytest.raises(ValueError):
        price_with_tax_00733(1000, -1)


def test_is_valid_sku_00733():
    assert is_valid_sku_00733("abc123")
    assert not is_valid_sku_00733("")


def test_bucket_by_tag_00733():
    p = Product_00733("s1", 100, ["a"])
    assert bucket_by_tag_00733([p]) == {"a": ["s1"]}
