"""Tests for catalog_00885."""

import pytest

from cartservice.generated.catalog_00885 import (
    Product_00885,
    bucket_by_tag_00885,
    is_valid_sku_00885,
    price_with_tax_00885,
)


def test_price_with_tax_00885():
    assert price_with_tax_00885(1000, 500) == 1050


def test_price_with_tax_negative_00885():
    with pytest.raises(ValueError):
        price_with_tax_00885(1000, -1)


def test_is_valid_sku_00885():
    assert is_valid_sku_00885("abc123")
    assert not is_valid_sku_00885("")


def test_bucket_by_tag_00885():
    p = Product_00885("s1", 100, ["a"])
    assert bucket_by_tag_00885([p]) == {"a": ["s1"]}
