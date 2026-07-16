"""Tests for catalog_01727."""

import pytest

from cartservice.generated.catalog_01727 import (
    Product_01727,
    bucket_by_tag_01727,
    is_valid_sku_01727,
    price_with_tax_01727,
)


def test_price_with_tax_01727():
    assert price_with_tax_01727(1000, 500) == 1050


def test_price_with_tax_negative_01727():
    with pytest.raises(ValueError):
        price_with_tax_01727(1000, -1)


def test_is_valid_sku_01727():
    assert is_valid_sku_01727("abc123")
    assert not is_valid_sku_01727("")


def test_bucket_by_tag_01727():
    p = Product_01727("s1", 100, ["a"])
    assert bucket_by_tag_01727([p]) == {"a": ["s1"]}
