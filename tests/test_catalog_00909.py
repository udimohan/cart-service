"""Tests for catalog_00909."""

import pytest

from cartservice.generated.catalog_00909 import (
    Product_00909,
    bucket_by_tag_00909,
    is_valid_sku_00909,
    price_with_tax_00909,
)


def test_price_with_tax_00909():
    assert price_with_tax_00909(1000, 500) == 1050


def test_price_with_tax_negative_00909():
    with pytest.raises(ValueError):
        price_with_tax_00909(1000, -1)


def test_is_valid_sku_00909():
    assert is_valid_sku_00909("abc123")
    assert not is_valid_sku_00909("")


def test_bucket_by_tag_00909():
    p = Product_00909("s1", 100, ["a"])
    assert bucket_by_tag_00909([p]) == {"a": ["s1"]}
