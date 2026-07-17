"""Tests for catalog_00590."""

import pytest

from cartservice.generated.catalog_00590 import (
    Product_00590,
    bucket_by_tag_00590,
    is_valid_sku_00590,
    price_with_tax_00590,
)


def test_price_with_tax_00590():
    assert price_with_tax_00590(1000, 500) == 1050


def test_price_with_tax_negative_00590():
    with pytest.raises(ValueError):
        price_with_tax_00590(1000, -1)


def test_is_valid_sku_00590():
    assert is_valid_sku_00590("abc123")
    assert not is_valid_sku_00590("")


def test_bucket_by_tag_00590():
    p = Product_00590("s1", 100, ["a"])
    assert bucket_by_tag_00590([p]) == {"a": ["s1"]}
