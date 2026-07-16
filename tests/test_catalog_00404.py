"""Tests for catalog_00404."""

import pytest

from cartservice.generated.catalog_00404 import (
    Product_00404,
    bucket_by_tag_00404,
    is_valid_sku_00404,
    price_with_tax_00404,
)


def test_price_with_tax_00404():
    assert price_with_tax_00404(1000, 500) == 1050


def test_price_with_tax_negative_00404():
    with pytest.raises(ValueError):
        price_with_tax_00404(1000, -1)


def test_is_valid_sku_00404():
    assert is_valid_sku_00404("abc123")
    assert not is_valid_sku_00404("")


def test_bucket_by_tag_00404():
    p = Product_00404("s1", 100, ["a"])
    assert bucket_by_tag_00404([p]) == {"a": ["s1"]}
