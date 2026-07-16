"""Tests for catalog_00432."""

import pytest

from cartservice.generated.catalog_00432 import (
    Product_00432,
    bucket_by_tag_00432,
    is_valid_sku_00432,
    price_with_tax_00432,
)


def test_price_with_tax_00432():
    assert price_with_tax_00432(1000, 500) == 1050


def test_price_with_tax_negative_00432():
    with pytest.raises(ValueError):
        price_with_tax_00432(1000, -1)


def test_is_valid_sku_00432():
    assert is_valid_sku_00432("abc123")
    assert not is_valid_sku_00432("")


def test_bucket_by_tag_00432():
    p = Product_00432("s1", 100, ["a"])
    assert bucket_by_tag_00432([p]) == {"a": ["s1"]}
