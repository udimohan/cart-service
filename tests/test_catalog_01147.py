"""Tests for catalog_01147."""

import pytest

from cartservice.generated.catalog_01147 import (
    Product_01147,
    bucket_by_tag_01147,
    is_valid_sku_01147,
    price_with_tax_01147,
)


def test_price_with_tax_01147():
    assert price_with_tax_01147(1000, 500) == 1050


def test_price_with_tax_negative_01147():
    with pytest.raises(ValueError):
        price_with_tax_01147(1000, -1)


def test_is_valid_sku_01147():
    assert is_valid_sku_01147("abc123")
    assert not is_valid_sku_01147("")


def test_bucket_by_tag_01147():
    p = Product_01147("s1", 100, ["a"])
    assert bucket_by_tag_01147([p]) == {"a": ["s1"]}
