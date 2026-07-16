"""Tests for catalog_00147."""

import pytest

from cartservice.generated.catalog_00147 import (
    Product_00147,
    bucket_by_tag_00147,
    is_valid_sku_00147,
    price_with_tax_00147,
)


def test_price_with_tax_00147():
    assert price_with_tax_00147(1000, 500) == 1050


def test_price_with_tax_negative_00147():
    with pytest.raises(ValueError):
        price_with_tax_00147(1000, -1)


def test_is_valid_sku_00147():
    assert is_valid_sku_00147("abc123")
    assert not is_valid_sku_00147("")


def test_bucket_by_tag_00147():
    p = Product_00147("s1", 100, ["a"])
    assert bucket_by_tag_00147([p]) == {"a": ["s1"]}
