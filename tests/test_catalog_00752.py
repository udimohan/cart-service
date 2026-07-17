"""Tests for catalog_00752."""

import pytest

from cartservice.generated.catalog_00752 import (
    Product_00752,
    bucket_by_tag_00752,
    is_valid_sku_00752,
    price_with_tax_00752,
)


def test_price_with_tax_00752():
    assert price_with_tax_00752(1000, 500) == 1050


def test_price_with_tax_negative_00752():
    with pytest.raises(ValueError):
        price_with_tax_00752(1000, -1)


def test_is_valid_sku_00752():
    assert is_valid_sku_00752("abc123")
    assert not is_valid_sku_00752("")


def test_bucket_by_tag_00752():
    p = Product_00752("s1", 100, ["a"])
    assert bucket_by_tag_00752([p]) == {"a": ["s1"]}
