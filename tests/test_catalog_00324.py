"""Tests for catalog_00324."""

import pytest

from cartservice.generated.catalog_00324 import (
    Product_00324,
    bucket_by_tag_00324,
    is_valid_sku_00324,
    price_with_tax_00324,
)


def test_price_with_tax_00324():
    assert price_with_tax_00324(1000, 500) == 1050


def test_price_with_tax_negative_00324():
    with pytest.raises(ValueError):
        price_with_tax_00324(1000, -1)


def test_is_valid_sku_00324():
    assert is_valid_sku_00324("abc123")
    assert not is_valid_sku_00324("")


def test_bucket_by_tag_00324():
    p = Product_00324("s1", 100, ["a"])
    assert bucket_by_tag_00324([p]) == {"a": ["s1"]}
