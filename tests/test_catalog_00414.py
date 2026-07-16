"""Tests for catalog_00414."""

import pytest

from cartservice.generated.catalog_00414 import (
    Product_00414,
    bucket_by_tag_00414,
    is_valid_sku_00414,
    price_with_tax_00414,
)


def test_price_with_tax_00414():
    assert price_with_tax_00414(1000, 500) == 1050


def test_price_with_tax_negative_00414():
    with pytest.raises(ValueError):
        price_with_tax_00414(1000, -1)


def test_is_valid_sku_00414():
    assert is_valid_sku_00414("abc123")
    assert not is_valid_sku_00414("")


def test_bucket_by_tag_00414():
    p = Product_00414("s1", 100, ["a"])
    assert bucket_by_tag_00414([p]) == {"a": ["s1"]}
