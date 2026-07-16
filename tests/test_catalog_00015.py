"""Tests for catalog_00015."""

import pytest

from cartservice.generated.catalog_00015 import (
    Product_00015,
    bucket_by_tag_00015,
    is_valid_sku_00015,
    price_with_tax_00015,
)


def test_price_with_tax_00015():
    assert price_with_tax_00015(1000, 500) == 1050


def test_price_with_tax_negative_00015():
    with pytest.raises(ValueError):
        price_with_tax_00015(1000, -1)


def test_is_valid_sku_00015():
    assert is_valid_sku_00015("abc123")
    assert not is_valid_sku_00015("")


def test_bucket_by_tag_00015():
    p = Product_00015("s1", 100, ["a"])
    assert bucket_by_tag_00015([p]) == {"a": ["s1"]}
