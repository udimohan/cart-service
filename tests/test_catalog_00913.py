"""Tests for catalog_00913."""

import pytest

from cartservice.generated.catalog_00913 import (
    Product_00913,
    bucket_by_tag_00913,
    is_valid_sku_00913,
    price_with_tax_00913,
)


def test_price_with_tax_00913():
    assert price_with_tax_00913(1000, 500) == 1050


def test_price_with_tax_negative_00913():
    with pytest.raises(ValueError):
        price_with_tax_00913(1000, -1)


def test_is_valid_sku_00913():
    assert is_valid_sku_00913("abc123")
    assert not is_valid_sku_00913("")


def test_bucket_by_tag_00913():
    p = Product_00913("s1", 100, ["a"])
    assert bucket_by_tag_00913([p]) == {"a": ["s1"]}
