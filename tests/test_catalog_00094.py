"""Tests for catalog_00094."""

import pytest

from cartservice.generated.catalog_00094 import (
    Product_00094,
    bucket_by_tag_00094,
    is_valid_sku_00094,
    price_with_tax_00094,
)


def test_price_with_tax_00094():
    assert price_with_tax_00094(1000, 500) == 1050


def test_price_with_tax_negative_00094():
    with pytest.raises(ValueError):
        price_with_tax_00094(1000, -1)


def test_is_valid_sku_00094():
    assert is_valid_sku_00094("abc123")
    assert not is_valid_sku_00094("")


def test_bucket_by_tag_00094():
    p = Product_00094("s1", 100, ["a"])
    assert bucket_by_tag_00094([p]) == {"a": ["s1"]}
