"""Tests for catalog_01324."""

import pytest

from cartservice.generated.catalog_01324 import (
    Product_01324,
    bucket_by_tag_01324,
    is_valid_sku_01324,
    price_with_tax_01324,
)


def test_price_with_tax_01324():
    assert price_with_tax_01324(1000, 500) == 1050


def test_price_with_tax_negative_01324():
    with pytest.raises(ValueError):
        price_with_tax_01324(1000, -1)


def test_is_valid_sku_01324():
    assert is_valid_sku_01324("abc123")
    assert not is_valid_sku_01324("")


def test_bucket_by_tag_01324():
    p = Product_01324("s1", 100, ["a"])
    assert bucket_by_tag_01324([p]) == {"a": ["s1"]}
