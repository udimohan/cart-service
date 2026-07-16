"""Tests for catalog_00200."""

import pytest

from cartservice.generated.catalog_00200 import (
    Product_00200,
    bucket_by_tag_00200,
    is_valid_sku_00200,
    price_with_tax_00200,
)


def test_price_with_tax_00200():
    assert price_with_tax_00200(1000, 500) == 1050


def test_price_with_tax_negative_00200():
    with pytest.raises(ValueError):
        price_with_tax_00200(1000, -1)


def test_is_valid_sku_00200():
    assert is_valid_sku_00200("abc123")
    assert not is_valid_sku_00200("")


def test_bucket_by_tag_00200():
    p = Product_00200("s1", 100, ["a"])
    assert bucket_by_tag_00200([p]) == {"a": ["s1"]}
