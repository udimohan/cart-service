"""Tests for catalog_01137."""

import pytest

from cartservice.generated.catalog_01137 import (
    Product_01137,
    bucket_by_tag_01137,
    is_valid_sku_01137,
    price_with_tax_01137,
)


def test_price_with_tax_01137():
    assert price_with_tax_01137(1000, 500) == 1050


def test_price_with_tax_negative_01137():
    with pytest.raises(ValueError):
        price_with_tax_01137(1000, -1)


def test_is_valid_sku_01137():
    assert is_valid_sku_01137("abc123")
    assert not is_valid_sku_01137("")


def test_bucket_by_tag_01137():
    p = Product_01137("s1", 100, ["a"])
    assert bucket_by_tag_01137([p]) == {"a": ["s1"]}
