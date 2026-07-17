"""Tests for catalog_00561."""

import pytest

from cartservice.generated.catalog_00561 import (
    Product_00561,
    bucket_by_tag_00561,
    is_valid_sku_00561,
    price_with_tax_00561,
)


def test_price_with_tax_00561():
    assert price_with_tax_00561(1000, 500) == 1050


def test_price_with_tax_negative_00561():
    with pytest.raises(ValueError):
        price_with_tax_00561(1000, -1)


def test_is_valid_sku_00561():
    assert is_valid_sku_00561("abc123")
    assert not is_valid_sku_00561("")


def test_bucket_by_tag_00561():
    p = Product_00561("s1", 100, ["a"])
    assert bucket_by_tag_00561([p]) == {"a": ["s1"]}
