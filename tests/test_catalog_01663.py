"""Tests for catalog_01663."""

import pytest

from cartservice.generated.catalog_01663 import (
    Product_01663,
    bucket_by_tag_01663,
    is_valid_sku_01663,
    price_with_tax_01663,
)


def test_price_with_tax_01663():
    assert price_with_tax_01663(1000, 500) == 1050


def test_price_with_tax_negative_01663():
    with pytest.raises(ValueError):
        price_with_tax_01663(1000, -1)


def test_is_valid_sku_01663():
    assert is_valid_sku_01663("abc123")
    assert not is_valid_sku_01663("")


def test_bucket_by_tag_01663():
    p = Product_01663("s1", 100, ["a"])
    assert bucket_by_tag_01663([p]) == {"a": ["s1"]}
