"""Tests for catalog_00989."""

import pytest

from cartservice.generated.catalog_00989 import (
    Product_00989,
    bucket_by_tag_00989,
    is_valid_sku_00989,
    price_with_tax_00989,
)


def test_price_with_tax_00989():
    assert price_with_tax_00989(1000, 500) == 1050


def test_price_with_tax_negative_00989():
    with pytest.raises(ValueError):
        price_with_tax_00989(1000, -1)


def test_is_valid_sku_00989():
    assert is_valid_sku_00989("abc123")
    assert not is_valid_sku_00989("")


def test_bucket_by_tag_00989():
    p = Product_00989("s1", 100, ["a"])
    assert bucket_by_tag_00989([p]) == {"a": ["s1"]}
