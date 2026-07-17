"""Tests for catalog_00072."""

import pytest

from cartservice.generated.catalog_00072 import (
    Product_00072,
    bucket_by_tag_00072,
    is_valid_sku_00072,
    price_with_tax_00072,
)


def test_price_with_tax_00072():
    assert price_with_tax_00072(1000, 500) == 1050


def test_price_with_tax_negative_00072():
    with pytest.raises(ValueError):
        price_with_tax_00072(1000, -1)


def test_is_valid_sku_00072():
    assert is_valid_sku_00072("abc123")
    assert not is_valid_sku_00072("")


def test_bucket_by_tag_00072():
    p = Product_00072("s1", 100, ["a"])
    assert bucket_by_tag_00072([p]) == {"a": ["s1"]}
