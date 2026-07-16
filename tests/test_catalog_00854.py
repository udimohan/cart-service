"""Tests for catalog_00854."""

import pytest

from cartservice.generated.catalog_00854 import (
    Product_00854,
    bucket_by_tag_00854,
    is_valid_sku_00854,
    price_with_tax_00854,
)


def test_price_with_tax_00854():
    assert price_with_tax_00854(1000, 500) == 1050


def test_price_with_tax_negative_00854():
    with pytest.raises(ValueError):
        price_with_tax_00854(1000, -1)


def test_is_valid_sku_00854():
    assert is_valid_sku_00854("abc123")
    assert not is_valid_sku_00854("")


def test_bucket_by_tag_00854():
    p = Product_00854("s1", 100, ["a"])
    assert bucket_by_tag_00854([p]) == {"a": ["s1"]}
