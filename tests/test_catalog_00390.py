"""Tests for catalog_00390."""

import pytest

from cartservice.generated.catalog_00390 import (
    Product_00390,
    bucket_by_tag_00390,
    is_valid_sku_00390,
    price_with_tax_00390,
)


def test_price_with_tax_00390():
    assert price_with_tax_00390(1000, 500) == 1050


def test_price_with_tax_negative_00390():
    with pytest.raises(ValueError):
        price_with_tax_00390(1000, -1)


def test_is_valid_sku_00390():
    assert is_valid_sku_00390("abc123")
    assert not is_valid_sku_00390("")


def test_bucket_by_tag_00390():
    p = Product_00390("s1", 100, ["a"])
    assert bucket_by_tag_00390([p]) == {"a": ["s1"]}
