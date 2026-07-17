"""Tests for catalog_00463."""

import pytest

from cartservice.generated.catalog_00463 import (
    Product_00463,
    bucket_by_tag_00463,
    is_valid_sku_00463,
    price_with_tax_00463,
)


def test_price_with_tax_00463():
    assert price_with_tax_00463(1000, 500) == 1050


def test_price_with_tax_negative_00463():
    with pytest.raises(ValueError):
        price_with_tax_00463(1000, -1)


def test_is_valid_sku_00463():
    assert is_valid_sku_00463("abc123")
    assert not is_valid_sku_00463("")


def test_bucket_by_tag_00463():
    p = Product_00463("s1", 100, ["a"])
    assert bucket_by_tag_00463([p]) == {"a": ["s1"]}
