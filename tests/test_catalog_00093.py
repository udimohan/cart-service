"""Tests for catalog_00093."""

import pytest

from cartservice.generated.catalog_00093 import (
    Product_00093,
    bucket_by_tag_00093,
    is_valid_sku_00093,
    price_with_tax_00093,
)


def test_price_with_tax_00093():
    assert price_with_tax_00093(1000, 500) == 1050


def test_price_with_tax_negative_00093():
    with pytest.raises(ValueError):
        price_with_tax_00093(1000, -1)


def test_is_valid_sku_00093():
    assert is_valid_sku_00093("abc123")
    assert not is_valid_sku_00093("")


def test_bucket_by_tag_00093():
    p = Product_00093("s1", 100, ["a"])
    assert bucket_by_tag_00093([p]) == {"a": ["s1"]}
