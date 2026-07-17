"""Tests for catalog_01006."""

import pytest

from cartservice.generated.catalog_01006 import (
    Product_01006,
    bucket_by_tag_01006,
    is_valid_sku_01006,
    price_with_tax_01006,
)


def test_price_with_tax_01006():
    assert price_with_tax_01006(1000, 500) == 1050


def test_price_with_tax_negative_01006():
    with pytest.raises(ValueError):
        price_with_tax_01006(1000, -1)


def test_is_valid_sku_01006():
    assert is_valid_sku_01006("abc123")
    assert not is_valid_sku_01006("")


def test_bucket_by_tag_01006():
    p = Product_01006("s1", 100, ["a"])
    assert bucket_by_tag_01006([p]) == {"a": ["s1"]}
