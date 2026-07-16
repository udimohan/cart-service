"""Tests for catalog_00807."""

import pytest

from cartservice.generated.catalog_00807 import (
    Product_00807,
    bucket_by_tag_00807,
    is_valid_sku_00807,
    price_with_tax_00807,
)


def test_price_with_tax_00807():
    assert price_with_tax_00807(1000, 500) == 1050


def test_price_with_tax_negative_00807():
    with pytest.raises(ValueError):
        price_with_tax_00807(1000, -1)


def test_is_valid_sku_00807():
    assert is_valid_sku_00807("abc123")
    assert not is_valid_sku_00807("")


def test_bucket_by_tag_00807():
    p = Product_00807("s1", 100, ["a"])
    assert bucket_by_tag_00807([p]) == {"a": ["s1"]}
