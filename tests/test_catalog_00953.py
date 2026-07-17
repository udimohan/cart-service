"""Tests for catalog_00953."""

import pytest

from cartservice.generated.catalog_00953 import (
    Product_00953,
    bucket_by_tag_00953,
    is_valid_sku_00953,
    price_with_tax_00953,
)


def test_price_with_tax_00953():
    assert price_with_tax_00953(1000, 500) == 1050


def test_price_with_tax_negative_00953():
    with pytest.raises(ValueError):
        price_with_tax_00953(1000, -1)


def test_is_valid_sku_00953():
    assert is_valid_sku_00953("abc123")
    assert not is_valid_sku_00953("")


def test_bucket_by_tag_00953():
    p = Product_00953("s1", 100, ["a"])
    assert bucket_by_tag_00953([p]) == {"a": ["s1"]}
