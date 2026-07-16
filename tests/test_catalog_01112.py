"""Tests for catalog_01112."""

import pytest

from cartservice.generated.catalog_01112 import (
    Product_01112,
    bucket_by_tag_01112,
    is_valid_sku_01112,
    price_with_tax_01112,
)


def test_price_with_tax_01112():
    assert price_with_tax_01112(1000, 500) == 1050


def test_price_with_tax_negative_01112():
    with pytest.raises(ValueError):
        price_with_tax_01112(1000, -1)


def test_is_valid_sku_01112():
    assert is_valid_sku_01112("abc123")
    assert not is_valid_sku_01112("")


def test_bucket_by_tag_01112():
    p = Product_01112("s1", 100, ["a"])
    assert bucket_by_tag_01112([p]) == {"a": ["s1"]}
