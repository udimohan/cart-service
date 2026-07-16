"""Tests for catalog_00202."""

import pytest

from cartservice.generated.catalog_00202 import (
    Product_00202,
    bucket_by_tag_00202,
    is_valid_sku_00202,
    price_with_tax_00202,
)


def test_price_with_tax_00202():
    assert price_with_tax_00202(1000, 500) == 1050


def test_price_with_tax_negative_00202():
    with pytest.raises(ValueError):
        price_with_tax_00202(1000, -1)


def test_is_valid_sku_00202():
    assert is_valid_sku_00202("abc123")
    assert not is_valid_sku_00202("")


def test_bucket_by_tag_00202():
    p = Product_00202("s1", 100, ["a"])
    assert bucket_by_tag_00202([p]) == {"a": ["s1"]}
