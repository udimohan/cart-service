"""Tests for catalog_00643."""

import pytest

from cartservice.generated.catalog_00643 import (
    Product_00643,
    bucket_by_tag_00643,
    is_valid_sku_00643,
    price_with_tax_00643,
)


def test_price_with_tax_00643():
    assert price_with_tax_00643(1000, 500) == 1050


def test_price_with_tax_negative_00643():
    with pytest.raises(ValueError):
        price_with_tax_00643(1000, -1)


def test_is_valid_sku_00643():
    assert is_valid_sku_00643("abc123")
    assert not is_valid_sku_00643("")


def test_bucket_by_tag_00643():
    p = Product_00643("s1", 100, ["a"])
    assert bucket_by_tag_00643([p]) == {"a": ["s1"]}
