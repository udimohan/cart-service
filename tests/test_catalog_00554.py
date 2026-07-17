"""Tests for catalog_00554."""

import pytest

from cartservice.generated.catalog_00554 import (
    Product_00554,
    bucket_by_tag_00554,
    is_valid_sku_00554,
    price_with_tax_00554,
)


def test_price_with_tax_00554():
    assert price_with_tax_00554(1000, 500) == 1050


def test_price_with_tax_negative_00554():
    with pytest.raises(ValueError):
        price_with_tax_00554(1000, -1)


def test_is_valid_sku_00554():
    assert is_valid_sku_00554("abc123")
    assert not is_valid_sku_00554("")


def test_bucket_by_tag_00554():
    p = Product_00554("s1", 100, ["a"])
    assert bucket_by_tag_00554([p]) == {"a": ["s1"]}
