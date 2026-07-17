"""Tests for catalog_01576."""

import pytest

from cartservice.generated.catalog_01576 import (
    Product_01576,
    bucket_by_tag_01576,
    is_valid_sku_01576,
    price_with_tax_01576,
)


def test_price_with_tax_01576():
    assert price_with_tax_01576(1000, 500) == 1050


def test_price_with_tax_negative_01576():
    with pytest.raises(ValueError):
        price_with_tax_01576(1000, -1)


def test_is_valid_sku_01576():
    assert is_valid_sku_01576("abc123")
    assert not is_valid_sku_01576("")


def test_bucket_by_tag_01576():
    p = Product_01576("s1", 100, ["a"])
    assert bucket_by_tag_01576([p]) == {"a": ["s1"]}
