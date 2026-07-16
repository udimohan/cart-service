"""Tests for catalog_01032."""

import pytest

from cartservice.generated.catalog_01032 import (
    Product_01032,
    bucket_by_tag_01032,
    is_valid_sku_01032,
    price_with_tax_01032,
)


def test_price_with_tax_01032():
    assert price_with_tax_01032(1000, 500) == 1050


def test_price_with_tax_negative_01032():
    with pytest.raises(ValueError):
        price_with_tax_01032(1000, -1)


def test_is_valid_sku_01032():
    assert is_valid_sku_01032("abc123")
    assert not is_valid_sku_01032("")


def test_bucket_by_tag_01032():
    p = Product_01032("s1", 100, ["a"])
    assert bucket_by_tag_01032([p]) == {"a": ["s1"]}
