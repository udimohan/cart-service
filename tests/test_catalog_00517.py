"""Tests for catalog_00517."""

import pytest

from cartservice.generated.catalog_00517 import (
    Product_00517,
    bucket_by_tag_00517,
    is_valid_sku_00517,
    price_with_tax_00517,
)


def test_price_with_tax_00517():
    assert price_with_tax_00517(1000, 500) == 1050


def test_price_with_tax_negative_00517():
    with pytest.raises(ValueError):
        price_with_tax_00517(1000, -1)


def test_is_valid_sku_00517():
    assert is_valid_sku_00517("abc123")
    assert not is_valid_sku_00517("")


def test_bucket_by_tag_00517():
    p = Product_00517("s1", 100, ["a"])
    assert bucket_by_tag_00517([p]) == {"a": ["s1"]}
