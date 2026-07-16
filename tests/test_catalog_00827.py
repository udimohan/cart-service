"""Tests for catalog_00827."""

import pytest

from cartservice.generated.catalog_00827 import (
    Product_00827,
    bucket_by_tag_00827,
    is_valid_sku_00827,
    price_with_tax_00827,
)


def test_price_with_tax_00827():
    assert price_with_tax_00827(1000, 500) == 1050


def test_price_with_tax_negative_00827():
    with pytest.raises(ValueError):
        price_with_tax_00827(1000, -1)


def test_is_valid_sku_00827():
    assert is_valid_sku_00827("abc123")
    assert not is_valid_sku_00827("")


def test_bucket_by_tag_00827():
    p = Product_00827("s1", 100, ["a"])
    assert bucket_by_tag_00827([p]) == {"a": ["s1"]}
