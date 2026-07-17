"""Tests for catalog_00078."""

import pytest

from cartservice.generated.catalog_00078 import (
    Product_00078,
    bucket_by_tag_00078,
    is_valid_sku_00078,
    price_with_tax_00078,
)


def test_price_with_tax_00078():
    assert price_with_tax_00078(1000, 500) == 1050


def test_price_with_tax_negative_00078():
    with pytest.raises(ValueError):
        price_with_tax_00078(1000, -1)


def test_is_valid_sku_00078():
    assert is_valid_sku_00078("abc123")
    assert not is_valid_sku_00078("")


def test_bucket_by_tag_00078():
    p = Product_00078("s1", 100, ["a"])
    assert bucket_by_tag_00078([p]) == {"a": ["s1"]}
