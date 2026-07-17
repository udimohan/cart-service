"""Tests for catalog_00729."""

import pytest

from cartservice.generated.catalog_00729 import (
    Product_00729,
    bucket_by_tag_00729,
    is_valid_sku_00729,
    price_with_tax_00729,
)


def test_price_with_tax_00729():
    assert price_with_tax_00729(1000, 500) == 1050


def test_price_with_tax_negative_00729():
    with pytest.raises(ValueError):
        price_with_tax_00729(1000, -1)


def test_is_valid_sku_00729():
    assert is_valid_sku_00729("abc123")
    assert not is_valid_sku_00729("")


def test_bucket_by_tag_00729():
    p = Product_00729("s1", 100, ["a"])
    assert bucket_by_tag_00729([p]) == {"a": ["s1"]}
