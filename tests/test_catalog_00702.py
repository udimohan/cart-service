"""Tests for catalog_00702."""

import pytest

from cartservice.generated.catalog_00702 import (
    Product_00702,
    bucket_by_tag_00702,
    is_valid_sku_00702,
    price_with_tax_00702,
)


def test_price_with_tax_00702():
    assert price_with_tax_00702(1000, 500) == 1050


def test_price_with_tax_negative_00702():
    with pytest.raises(ValueError):
        price_with_tax_00702(1000, -1)


def test_is_valid_sku_00702():
    assert is_valid_sku_00702("abc123")
    assert not is_valid_sku_00702("")


def test_bucket_by_tag_00702():
    p = Product_00702("s1", 100, ["a"])
    assert bucket_by_tag_00702([p]) == {"a": ["s1"]}
