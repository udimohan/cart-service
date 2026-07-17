"""Tests for catalog_00545."""

import pytest

from cartservice.generated.catalog_00545 import (
    Product_00545,
    bucket_by_tag_00545,
    is_valid_sku_00545,
    price_with_tax_00545,
)


def test_price_with_tax_00545():
    assert price_with_tax_00545(1000, 500) == 1050


def test_price_with_tax_negative_00545():
    with pytest.raises(ValueError):
        price_with_tax_00545(1000, -1)


def test_is_valid_sku_00545():
    assert is_valid_sku_00545("abc123")
    assert not is_valid_sku_00545("")


def test_bucket_by_tag_00545():
    p = Product_00545("s1", 100, ["a"])
    assert bucket_by_tag_00545([p]) == {"a": ["s1"]}
