"""Tests for catalog_00273."""

import pytest

from cartservice.generated.catalog_00273 import (
    Product_00273,
    bucket_by_tag_00273,
    is_valid_sku_00273,
    price_with_tax_00273,
)


def test_price_with_tax_00273():
    assert price_with_tax_00273(1000, 500) == 1050


def test_price_with_tax_negative_00273():
    with pytest.raises(ValueError):
        price_with_tax_00273(1000, -1)


def test_is_valid_sku_00273():
    assert is_valid_sku_00273("abc123")
    assert not is_valid_sku_00273("")


def test_bucket_by_tag_00273():
    p = Product_00273("s1", 100, ["a"])
    assert bucket_by_tag_00273([p]) == {"a": ["s1"]}
