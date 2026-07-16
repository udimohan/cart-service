"""Tests for catalog_00904."""

import pytest

from cartservice.generated.catalog_00904 import (
    Product_00904,
    bucket_by_tag_00904,
    is_valid_sku_00904,
    price_with_tax_00904,
)


def test_price_with_tax_00904():
    assert price_with_tax_00904(1000, 500) == 1050


def test_price_with_tax_negative_00904():
    with pytest.raises(ValueError):
        price_with_tax_00904(1000, -1)


def test_is_valid_sku_00904():
    assert is_valid_sku_00904("abc123")
    assert not is_valid_sku_00904("")


def test_bucket_by_tag_00904():
    p = Product_00904("s1", 100, ["a"])
    assert bucket_by_tag_00904([p]) == {"a": ["s1"]}
