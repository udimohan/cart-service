"""Tests for catalog_00998."""

import pytest

from cartservice.generated.catalog_00998 import (
    Product_00998,
    bucket_by_tag_00998,
    is_valid_sku_00998,
    price_with_tax_00998,
)


def test_price_with_tax_00998():
    assert price_with_tax_00998(1000, 500) == 1050


def test_price_with_tax_negative_00998():
    with pytest.raises(ValueError):
        price_with_tax_00998(1000, -1)


def test_is_valid_sku_00998():
    assert is_valid_sku_00998("abc123")
    assert not is_valid_sku_00998("")


def test_bucket_by_tag_00998():
    p = Product_00998("s1", 100, ["a"])
    assert bucket_by_tag_00998([p]) == {"a": ["s1"]}
