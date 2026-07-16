"""Tests for catalog_00576."""

import pytest

from cartservice.generated.catalog_00576 import (
    Product_00576,
    bucket_by_tag_00576,
    is_valid_sku_00576,
    price_with_tax_00576,
)


def test_price_with_tax_00576():
    assert price_with_tax_00576(1000, 500) == 1050


def test_price_with_tax_negative_00576():
    with pytest.raises(ValueError):
        price_with_tax_00576(1000, -1)


def test_is_valid_sku_00576():
    assert is_valid_sku_00576("abc123")
    assert not is_valid_sku_00576("")


def test_bucket_by_tag_00576():
    p = Product_00576("s1", 100, ["a"])
    assert bucket_by_tag_00576([p]) == {"a": ["s1"]}
