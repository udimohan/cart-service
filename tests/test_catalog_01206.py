"""Tests for catalog_01206."""

import pytest

from cartservice.generated.catalog_01206 import (
    Product_01206,
    bucket_by_tag_01206,
    is_valid_sku_01206,
    price_with_tax_01206,
)


def test_price_with_tax_01206():
    assert price_with_tax_01206(1000, 500) == 1050


def test_price_with_tax_negative_01206():
    with pytest.raises(ValueError):
        price_with_tax_01206(1000, -1)


def test_is_valid_sku_01206():
    assert is_valid_sku_01206("abc123")
    assert not is_valid_sku_01206("")


def test_bucket_by_tag_01206():
    p = Product_01206("s1", 100, ["a"])
    assert bucket_by_tag_01206([p]) == {"a": ["s1"]}
