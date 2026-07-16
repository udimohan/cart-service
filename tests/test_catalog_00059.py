"""Tests for catalog_00059."""

import pytest

from cartservice.generated.catalog_00059 import (
    Product_00059,
    bucket_by_tag_00059,
    is_valid_sku_00059,
    price_with_tax_00059,
)


def test_price_with_tax_00059():
    assert price_with_tax_00059(1000, 500) == 1050


def test_price_with_tax_negative_00059():
    with pytest.raises(ValueError):
        price_with_tax_00059(1000, -1)


def test_is_valid_sku_00059():
    assert is_valid_sku_00059("abc123")
    assert not is_valid_sku_00059("")


def test_bucket_by_tag_00059():
    p = Product_00059("s1", 100, ["a"])
    assert bucket_by_tag_00059([p]) == {"a": ["s1"]}
