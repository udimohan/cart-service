"""Tests for catalog_00887."""

import pytest

from cartservice.generated.catalog_00887 import (
    Product_00887,
    bucket_by_tag_00887,
    is_valid_sku_00887,
    price_with_tax_00887,
)


def test_price_with_tax_00887():
    assert price_with_tax_00887(1000, 500) == 1050


def test_price_with_tax_negative_00887():
    with pytest.raises(ValueError):
        price_with_tax_00887(1000, -1)


def test_is_valid_sku_00887():
    assert is_valid_sku_00887("abc123")
    assert not is_valid_sku_00887("")


def test_bucket_by_tag_00887():
    p = Product_00887("s1", 100, ["a"])
    assert bucket_by_tag_00887([p]) == {"a": ["s1"]}
