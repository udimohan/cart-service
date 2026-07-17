"""Tests for catalog_00396."""

import pytest

from cartservice.generated.catalog_00396 import (
    Product_00396,
    bucket_by_tag_00396,
    is_valid_sku_00396,
    price_with_tax_00396,
)


def test_price_with_tax_00396():
    assert price_with_tax_00396(1000, 500) == 1050


def test_price_with_tax_negative_00396():
    with pytest.raises(ValueError):
        price_with_tax_00396(1000, -1)


def test_is_valid_sku_00396():
    assert is_valid_sku_00396("abc123")
    assert not is_valid_sku_00396("")


def test_bucket_by_tag_00396():
    p = Product_00396("s1", 100, ["a"])
    assert bucket_by_tag_00396([p]) == {"a": ["s1"]}
