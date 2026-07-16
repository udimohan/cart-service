"""Tests for catalog_00697."""

import pytest

from cartservice.generated.catalog_00697 import (
    Product_00697,
    bucket_by_tag_00697,
    is_valid_sku_00697,
    price_with_tax_00697,
)


def test_price_with_tax_00697():
    assert price_with_tax_00697(1000, 500) == 1050


def test_price_with_tax_negative_00697():
    with pytest.raises(ValueError):
        price_with_tax_00697(1000, -1)


def test_is_valid_sku_00697():
    assert is_valid_sku_00697("abc123")
    assert not is_valid_sku_00697("")


def test_bucket_by_tag_00697():
    p = Product_00697("s1", 100, ["a"])
    assert bucket_by_tag_00697([p]) == {"a": ["s1"]}
