"""Tests for catalog_00087."""

import pytest

from cartservice.generated.catalog_00087 import (
    Product_00087,
    bucket_by_tag_00087,
    is_valid_sku_00087,
    price_with_tax_00087,
)


def test_price_with_tax_00087():
    assert price_with_tax_00087(1000, 500) == 1050


def test_price_with_tax_negative_00087():
    with pytest.raises(ValueError):
        price_with_tax_00087(1000, -1)


def test_is_valid_sku_00087():
    assert is_valid_sku_00087("abc123")
    assert not is_valid_sku_00087("")


def test_bucket_by_tag_00087():
    p = Product_00087("s1", 100, ["a"])
    assert bucket_by_tag_00087([p]) == {"a": ["s1"]}
