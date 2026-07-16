"""Tests for catalog_01305."""

import pytest

from cartservice.generated.catalog_01305 import (
    Product_01305,
    bucket_by_tag_01305,
    is_valid_sku_01305,
    price_with_tax_01305,
)


def test_price_with_tax_01305():
    assert price_with_tax_01305(1000, 500) == 1050


def test_price_with_tax_negative_01305():
    with pytest.raises(ValueError):
        price_with_tax_01305(1000, -1)


def test_is_valid_sku_01305():
    assert is_valid_sku_01305("abc123")
    assert not is_valid_sku_01305("")


def test_bucket_by_tag_01305():
    p = Product_01305("s1", 100, ["a"])
    assert bucket_by_tag_01305([p]) == {"a": ["s1"]}
