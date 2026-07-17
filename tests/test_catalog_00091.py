"""Tests for catalog_00091."""

import pytest

from cartservice.generated.catalog_00091 import (
    Product_00091,
    bucket_by_tag_00091,
    is_valid_sku_00091,
    price_with_tax_00091,
)


def test_price_with_tax_00091():
    assert price_with_tax_00091(1000, 500) == 1050


def test_price_with_tax_negative_00091():
    with pytest.raises(ValueError):
        price_with_tax_00091(1000, -1)


def test_is_valid_sku_00091():
    assert is_valid_sku_00091("abc123")
    assert not is_valid_sku_00091("")


def test_bucket_by_tag_00091():
    p = Product_00091("s1", 100, ["a"])
    assert bucket_by_tag_00091([p]) == {"a": ["s1"]}
