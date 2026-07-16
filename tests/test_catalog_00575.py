"""Tests for catalog_00575."""

import pytest

from cartservice.generated.catalog_00575 import (
    Product_00575,
    bucket_by_tag_00575,
    is_valid_sku_00575,
    price_with_tax_00575,
)


def test_price_with_tax_00575():
    assert price_with_tax_00575(1000, 500) == 1050


def test_price_with_tax_negative_00575():
    with pytest.raises(ValueError):
        price_with_tax_00575(1000, -1)


def test_is_valid_sku_00575():
    assert is_valid_sku_00575("abc123")
    assert not is_valid_sku_00575("")


def test_bucket_by_tag_00575():
    p = Product_00575("s1", 100, ["a"])
    assert bucket_by_tag_00575([p]) == {"a": ["s1"]}
