"""Tests for catalog_01498."""

import pytest

from cartservice.generated.catalog_01498 import (
    Product_01498,
    bucket_by_tag_01498,
    is_valid_sku_01498,
    price_with_tax_01498,
)


def test_price_with_tax_01498():
    assert price_with_tax_01498(1000, 500) == 1050


def test_price_with_tax_negative_01498():
    with pytest.raises(ValueError):
        price_with_tax_01498(1000, -1)


def test_is_valid_sku_01498():
    assert is_valid_sku_01498("abc123")
    assert not is_valid_sku_01498("")


def test_bucket_by_tag_01498():
    p = Product_01498("s1", 100, ["a"])
    assert bucket_by_tag_01498([p]) == {"a": ["s1"]}
