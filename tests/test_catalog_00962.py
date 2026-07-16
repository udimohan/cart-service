"""Tests for catalog_00962."""

import pytest

from cartservice.generated.catalog_00962 import (
    Product_00962,
    bucket_by_tag_00962,
    is_valid_sku_00962,
    price_with_tax_00962,
)


def test_price_with_tax_00962():
    assert price_with_tax_00962(1000, 500) == 1050


def test_price_with_tax_negative_00962():
    with pytest.raises(ValueError):
        price_with_tax_00962(1000, -1)


def test_is_valid_sku_00962():
    assert is_valid_sku_00962("abc123")
    assert not is_valid_sku_00962("")


def test_bucket_by_tag_00962():
    p = Product_00962("s1", 100, ["a"])
    assert bucket_by_tag_00962([p]) == {"a": ["s1"]}
