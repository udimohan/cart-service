"""Tests for catalog_00204."""

import pytest

from cartservice.generated.catalog_00204 import (
    Product_00204,
    bucket_by_tag_00204,
    is_valid_sku_00204,
    price_with_tax_00204,
)


def test_price_with_tax_00204():
    assert price_with_tax_00204(1000, 500) == 1050


def test_price_with_tax_negative_00204():
    with pytest.raises(ValueError):
        price_with_tax_00204(1000, -1)


def test_is_valid_sku_00204():
    assert is_valid_sku_00204("abc123")
    assert not is_valid_sku_00204("")


def test_bucket_by_tag_00204():
    p = Product_00204("s1", 100, ["a"])
    assert bucket_by_tag_00204([p]) == {"a": ["s1"]}
