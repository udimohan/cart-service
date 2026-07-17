"""Tests for catalog_00986."""

import pytest

from cartservice.generated.catalog_00986 import (
    Product_00986,
    bucket_by_tag_00986,
    is_valid_sku_00986,
    price_with_tax_00986,
)


def test_price_with_tax_00986():
    assert price_with_tax_00986(1000, 500) == 1050


def test_price_with_tax_negative_00986():
    with pytest.raises(ValueError):
        price_with_tax_00986(1000, -1)


def test_is_valid_sku_00986():
    assert is_valid_sku_00986("abc123")
    assert not is_valid_sku_00986("")


def test_bucket_by_tag_00986():
    p = Product_00986("s1", 100, ["a"])
    assert bucket_by_tag_00986([p]) == {"a": ["s1"]}
