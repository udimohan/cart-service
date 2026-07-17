"""Tests for catalog_00696."""

import pytest

from cartservice.generated.catalog_00696 import (
    Product_00696,
    bucket_by_tag_00696,
    is_valid_sku_00696,
    price_with_tax_00696,
)


def test_price_with_tax_00696():
    assert price_with_tax_00696(1000, 500) == 1050


def test_price_with_tax_negative_00696():
    with pytest.raises(ValueError):
        price_with_tax_00696(1000, -1)


def test_is_valid_sku_00696():
    assert is_valid_sku_00696("abc123")
    assert not is_valid_sku_00696("")


def test_bucket_by_tag_00696():
    p = Product_00696("s1", 100, ["a"])
    assert bucket_by_tag_00696([p]) == {"a": ["s1"]}
