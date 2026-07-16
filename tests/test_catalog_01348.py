"""Tests for catalog_01348."""

import pytest

from cartservice.generated.catalog_01348 import (
    Product_01348,
    bucket_by_tag_01348,
    is_valid_sku_01348,
    price_with_tax_01348,
)


def test_price_with_tax_01348():
    assert price_with_tax_01348(1000, 500) == 1050


def test_price_with_tax_negative_01348():
    with pytest.raises(ValueError):
        price_with_tax_01348(1000, -1)


def test_is_valid_sku_01348():
    assert is_valid_sku_01348("abc123")
    assert not is_valid_sku_01348("")


def test_bucket_by_tag_01348():
    p = Product_01348("s1", 100, ["a"])
    assert bucket_by_tag_01348([p]) == {"a": ["s1"]}
