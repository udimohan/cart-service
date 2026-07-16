"""Tests for catalog_00086."""

import pytest

from cartservice.generated.catalog_00086 import (
    Product_00086,
    bucket_by_tag_00086,
    is_valid_sku_00086,
    price_with_tax_00086,
)


def test_price_with_tax_00086():
    assert price_with_tax_00086(1000, 500) == 1050


def test_price_with_tax_negative_00086():
    with pytest.raises(ValueError):
        price_with_tax_00086(1000, -1)


def test_is_valid_sku_00086():
    assert is_valid_sku_00086("abc123")
    assert not is_valid_sku_00086("")


def test_bucket_by_tag_00086():
    p = Product_00086("s1", 100, ["a"])
    assert bucket_by_tag_00086([p]) == {"a": ["s1"]}
