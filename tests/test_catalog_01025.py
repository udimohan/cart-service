"""Tests for catalog_01025."""

import pytest

from cartservice.generated.catalog_01025 import (
    Product_01025,
    bucket_by_tag_01025,
    is_valid_sku_01025,
    price_with_tax_01025,
)


def test_price_with_tax_01025():
    assert price_with_tax_01025(1000, 500) == 1050


def test_price_with_tax_negative_01025():
    with pytest.raises(ValueError):
        price_with_tax_01025(1000, -1)


def test_is_valid_sku_01025():
    assert is_valid_sku_01025("abc123")
    assert not is_valid_sku_01025("")


def test_bucket_by_tag_01025():
    p = Product_01025("s1", 100, ["a"])
    assert bucket_by_tag_01025([p]) == {"a": ["s1"]}
