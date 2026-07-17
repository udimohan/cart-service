"""Tests for catalog_00034."""

import pytest

from cartservice.generated.catalog_00034 import (
    Product_00034,
    bucket_by_tag_00034,
    is_valid_sku_00034,
    price_with_tax_00034,
)


def test_price_with_tax_00034():
    assert price_with_tax_00034(1000, 500) == 1050


def test_price_with_tax_negative_00034():
    with pytest.raises(ValueError):
        price_with_tax_00034(1000, -1)


def test_is_valid_sku_00034():
    assert is_valid_sku_00034("abc123")
    assert not is_valid_sku_00034("")


def test_bucket_by_tag_00034():
    p = Product_00034("s1", 100, ["a"])
    assert bucket_by_tag_00034([p]) == {"a": ["s1"]}
