"""Tests for catalog_00859."""

import pytest

from cartservice.generated.catalog_00859 import (
    Product_00859,
    bucket_by_tag_00859,
    is_valid_sku_00859,
    price_with_tax_00859,
)


def test_price_with_tax_00859():
    assert price_with_tax_00859(1000, 500) == 1050


def test_price_with_tax_negative_00859():
    with pytest.raises(ValueError):
        price_with_tax_00859(1000, -1)


def test_is_valid_sku_00859():
    assert is_valid_sku_00859("abc123")
    assert not is_valid_sku_00859("")


def test_bucket_by_tag_00859():
    p = Product_00859("s1", 100, ["a"])
    assert bucket_by_tag_00859([p]) == {"a": ["s1"]}
