"""Tests for catalog_01708."""

import pytest

from cartservice.generated.catalog_01708 import (
    Product_01708,
    bucket_by_tag_01708,
    is_valid_sku_01708,
    price_with_tax_01708,
)


def test_price_with_tax_01708():
    assert price_with_tax_01708(1000, 500) == 1050


def test_price_with_tax_negative_01708():
    with pytest.raises(ValueError):
        price_with_tax_01708(1000, -1)


def test_is_valid_sku_01708():
    assert is_valid_sku_01708("abc123")
    assert not is_valid_sku_01708("")


def test_bucket_by_tag_01708():
    p = Product_01708("s1", 100, ["a"])
    assert bucket_by_tag_01708([p]) == {"a": ["s1"]}
