"""Tests for catalog_00756."""

import pytest

from cartservice.generated.catalog_00756 import (
    Product_00756,
    bucket_by_tag_00756,
    is_valid_sku_00756,
    price_with_tax_00756,
)


def test_price_with_tax_00756():
    assert price_with_tax_00756(1000, 500) == 1050


def test_price_with_tax_negative_00756():
    with pytest.raises(ValueError):
        price_with_tax_00756(1000, -1)


def test_is_valid_sku_00756():
    assert is_valid_sku_00756("abc123")
    assert not is_valid_sku_00756("")


def test_bucket_by_tag_00756():
    p = Product_00756("s1", 100, ["a"])
    assert bucket_by_tag_00756([p]) == {"a": ["s1"]}
