"""Tests for catalog_00041."""

import pytest

from cartservice.generated.catalog_00041 import (
    Product_00041,
    bucket_by_tag_00041,
    is_valid_sku_00041,
    price_with_tax_00041,
)


def test_price_with_tax_00041():
    assert price_with_tax_00041(1000, 500) == 1050


def test_price_with_tax_negative_00041():
    with pytest.raises(ValueError):
        price_with_tax_00041(1000, -1)


def test_is_valid_sku_00041():
    assert is_valid_sku_00041("abc123")
    assert not is_valid_sku_00041("")


def test_bucket_by_tag_00041():
    p = Product_00041("s1", 100, ["a"])
    assert bucket_by_tag_00041([p]) == {"a": ["s1"]}
