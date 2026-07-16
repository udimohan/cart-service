"""Tests for catalog_00481."""

import pytest

from cartservice.generated.catalog_00481 import (
    Product_00481,
    bucket_by_tag_00481,
    is_valid_sku_00481,
    price_with_tax_00481,
)


def test_price_with_tax_00481():
    assert price_with_tax_00481(1000, 500) == 1050


def test_price_with_tax_negative_00481():
    with pytest.raises(ValueError):
        price_with_tax_00481(1000, -1)


def test_is_valid_sku_00481():
    assert is_valid_sku_00481("abc123")
    assert not is_valid_sku_00481("")


def test_bucket_by_tag_00481():
    p = Product_00481("s1", 100, ["a"])
    assert bucket_by_tag_00481([p]) == {"a": ["s1"]}
