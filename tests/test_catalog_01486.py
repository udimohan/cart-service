"""Tests for catalog_01486."""

import pytest

from cartservice.generated.catalog_01486 import (
    Product_01486,
    bucket_by_tag_01486,
    is_valid_sku_01486,
    price_with_tax_01486,
)


def test_price_with_tax_01486():
    assert price_with_tax_01486(1000, 500) == 1050


def test_price_with_tax_negative_01486():
    with pytest.raises(ValueError):
        price_with_tax_01486(1000, -1)


def test_is_valid_sku_01486():
    assert is_valid_sku_01486("abc123")
    assert not is_valid_sku_01486("")


def test_bucket_by_tag_01486():
    p = Product_01486("s1", 100, ["a"])
    assert bucket_by_tag_01486([p]) == {"a": ["s1"]}
