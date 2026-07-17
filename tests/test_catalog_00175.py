"""Tests for catalog_00175."""

import pytest

from cartservice.generated.catalog_00175 import (
    Product_00175,
    bucket_by_tag_00175,
    is_valid_sku_00175,
    price_with_tax_00175,
)


def test_price_with_tax_00175():
    assert price_with_tax_00175(1000, 500) == 1050


def test_price_with_tax_negative_00175():
    with pytest.raises(ValueError):
        price_with_tax_00175(1000, -1)


def test_is_valid_sku_00175():
    assert is_valid_sku_00175("abc123")
    assert not is_valid_sku_00175("")


def test_bucket_by_tag_00175():
    p = Product_00175("s1", 100, ["a"])
    assert bucket_by_tag_00175([p]) == {"a": ["s1"]}
