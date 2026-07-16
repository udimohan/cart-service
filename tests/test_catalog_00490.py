"""Tests for catalog_00490."""

import pytest

from cartservice.generated.catalog_00490 import (
    Product_00490,
    bucket_by_tag_00490,
    is_valid_sku_00490,
    price_with_tax_00490,
)


def test_price_with_tax_00490():
    assert price_with_tax_00490(1000, 500) == 1050


def test_price_with_tax_negative_00490():
    with pytest.raises(ValueError):
        price_with_tax_00490(1000, -1)


def test_is_valid_sku_00490():
    assert is_valid_sku_00490("abc123")
    assert not is_valid_sku_00490("")


def test_bucket_by_tag_00490():
    p = Product_00490("s1", 100, ["a"])
    assert bucket_by_tag_00490([p]) == {"a": ["s1"]}
