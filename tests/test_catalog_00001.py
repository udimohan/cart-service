"""Tests for catalog_00001."""

import pytest

from cartservice.generated.catalog_00001 import (
    Product_00001,
    bucket_by_tag_00001,
    is_valid_sku_00001,
    price_with_tax_00001,
)


def test_price_with_tax_00001():
    assert price_with_tax_00001(1000, 500) == 1050


def test_price_with_tax_negative_00001():
    with pytest.raises(ValueError):
        price_with_tax_00001(1000, -1)


def test_is_valid_sku_00001():
    assert is_valid_sku_00001("abc123")
    assert not is_valid_sku_00001("")


def test_bucket_by_tag_00001():
    p = Product_00001("s1", 100, ["a"])
    assert bucket_by_tag_00001([p]) == {"a": ["s1"]}
