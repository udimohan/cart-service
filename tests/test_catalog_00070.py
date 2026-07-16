"""Tests for catalog_00070."""

import pytest

from cartservice.generated.catalog_00070 import (
    Product_00070,
    bucket_by_tag_00070,
    is_valid_sku_00070,
    price_with_tax_00070,
)


def test_price_with_tax_00070():
    assert price_with_tax_00070(1000, 500) == 1050


def test_price_with_tax_negative_00070():
    with pytest.raises(ValueError):
        price_with_tax_00070(1000, -1)


def test_is_valid_sku_00070():
    assert is_valid_sku_00070("abc123")
    assert not is_valid_sku_00070("")


def test_bucket_by_tag_00070():
    p = Product_00070("s1", 100, ["a"])
    assert bucket_by_tag_00070([p]) == {"a": ["s1"]}
