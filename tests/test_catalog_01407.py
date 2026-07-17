"""Tests for catalog_01407."""

import pytest

from cartservice.generated.catalog_01407 import (
    Product_01407,
    bucket_by_tag_01407,
    is_valid_sku_01407,
    price_with_tax_01407,
)


def test_price_with_tax_01407():
    assert price_with_tax_01407(1000, 500) == 1050


def test_price_with_tax_negative_01407():
    with pytest.raises(ValueError):
        price_with_tax_01407(1000, -1)


def test_is_valid_sku_01407():
    assert is_valid_sku_01407("abc123")
    assert not is_valid_sku_01407("")


def test_bucket_by_tag_01407():
    p = Product_01407("s1", 100, ["a"])
    assert bucket_by_tag_01407([p]) == {"a": ["s1"]}
