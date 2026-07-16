"""Tests for catalog_00126."""

import pytest

from cartservice.generated.catalog_00126 import (
    Product_00126,
    bucket_by_tag_00126,
    is_valid_sku_00126,
    price_with_tax_00126,
)


def test_price_with_tax_00126():
    assert price_with_tax_00126(1000, 500) == 1050


def test_price_with_tax_negative_00126():
    with pytest.raises(ValueError):
        price_with_tax_00126(1000, -1)


def test_is_valid_sku_00126():
    assert is_valid_sku_00126("abc123")
    assert not is_valid_sku_00126("")


def test_bucket_by_tag_00126():
    p = Product_00126("s1", 100, ["a"])
    assert bucket_by_tag_00126([p]) == {"a": ["s1"]}
