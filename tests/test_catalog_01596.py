"""Tests for catalog_01596."""

import pytest

from cartservice.generated.catalog_01596 import (
    Product_01596,
    bucket_by_tag_01596,
    is_valid_sku_01596,
    price_with_tax_01596,
)


def test_price_with_tax_01596():
    assert price_with_tax_01596(1000, 500) == 1050


def test_price_with_tax_negative_01596():
    with pytest.raises(ValueError):
        price_with_tax_01596(1000, -1)


def test_is_valid_sku_01596():
    assert is_valid_sku_01596("abc123")
    assert not is_valid_sku_01596("")


def test_bucket_by_tag_01596():
    p = Product_01596("s1", 100, ["a"])
    assert bucket_by_tag_01596([p]) == {"a": ["s1"]}
