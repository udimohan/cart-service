"""Tests for catalog_00810."""

import pytest

from cartservice.generated.catalog_00810 import (
    Product_00810,
    bucket_by_tag_00810,
    is_valid_sku_00810,
    price_with_tax_00810,
)


def test_price_with_tax_00810():
    assert price_with_tax_00810(1000, 500) == 1050


def test_price_with_tax_negative_00810():
    with pytest.raises(ValueError):
        price_with_tax_00810(1000, -1)


def test_is_valid_sku_00810():
    assert is_valid_sku_00810("abc123")
    assert not is_valid_sku_00810("")


def test_bucket_by_tag_00810():
    p = Product_00810("s1", 100, ["a"])
    assert bucket_by_tag_00810([p]) == {"a": ["s1"]}
