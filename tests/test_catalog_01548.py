"""Tests for catalog_01548."""

import pytest

from cartservice.generated.catalog_01548 import (
    Product_01548,
    bucket_by_tag_01548,
    is_valid_sku_01548,
    price_with_tax_01548,
)


def test_price_with_tax_01548():
    assert price_with_tax_01548(1000, 500) == 1050


def test_price_with_tax_negative_01548():
    with pytest.raises(ValueError):
        price_with_tax_01548(1000, -1)


def test_is_valid_sku_01548():
    assert is_valid_sku_01548("abc123")
    assert not is_valid_sku_01548("")


def test_bucket_by_tag_01548():
    p = Product_01548("s1", 100, ["a"])
    assert bucket_by_tag_01548([p]) == {"a": ["s1"]}
