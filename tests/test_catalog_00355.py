"""Tests for catalog_00355."""

import pytest

from cartservice.generated.catalog_00355 import (
    Product_00355,
    bucket_by_tag_00355,
    is_valid_sku_00355,
    price_with_tax_00355,
)


def test_price_with_tax_00355():
    assert price_with_tax_00355(1000, 500) == 1050


def test_price_with_tax_negative_00355():
    with pytest.raises(ValueError):
        price_with_tax_00355(1000, -1)


def test_is_valid_sku_00355():
    assert is_valid_sku_00355("abc123")
    assert not is_valid_sku_00355("")


def test_bucket_by_tag_00355():
    p = Product_00355("s1", 100, ["a"])
    assert bucket_by_tag_00355([p]) == {"a": ["s1"]}
