"""Tests for catalog_00429."""

import pytest

from cartservice.generated.catalog_00429 import (
    Product_00429,
    bucket_by_tag_00429,
    is_valid_sku_00429,
    price_with_tax_00429,
)


def test_price_with_tax_00429():
    assert price_with_tax_00429(1000, 500) == 1050


def test_price_with_tax_negative_00429():
    with pytest.raises(ValueError):
        price_with_tax_00429(1000, -1)


def test_is_valid_sku_00429():
    assert is_valid_sku_00429("abc123")
    assert not is_valid_sku_00429("")


def test_bucket_by_tag_00429():
    p = Product_00429("s1", 100, ["a"])
    assert bucket_by_tag_00429([p]) == {"a": ["s1"]}
