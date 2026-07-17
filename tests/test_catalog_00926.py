"""Tests for catalog_00926."""

import pytest

from cartservice.generated.catalog_00926 import (
    Product_00926,
    bucket_by_tag_00926,
    is_valid_sku_00926,
    price_with_tax_00926,
)


def test_price_with_tax_00926():
    assert price_with_tax_00926(1000, 500) == 1050


def test_price_with_tax_negative_00926():
    with pytest.raises(ValueError):
        price_with_tax_00926(1000, -1)


def test_is_valid_sku_00926():
    assert is_valid_sku_00926("abc123")
    assert not is_valid_sku_00926("")


def test_bucket_by_tag_00926():
    p = Product_00926("s1", 100, ["a"])
    assert bucket_by_tag_00926([p]) == {"a": ["s1"]}
