"""Tests for catalog_00787."""

import pytest

from cartservice.generated.catalog_00787 import (
    Product_00787,
    bucket_by_tag_00787,
    is_valid_sku_00787,
    price_with_tax_00787,
)


def test_price_with_tax_00787():
    assert price_with_tax_00787(1000, 500) == 1050


def test_price_with_tax_negative_00787():
    with pytest.raises(ValueError):
        price_with_tax_00787(1000, -1)


def test_is_valid_sku_00787():
    assert is_valid_sku_00787("abc123")
    assert not is_valid_sku_00787("")


def test_bucket_by_tag_00787():
    p = Product_00787("s1", 100, ["a"])
    assert bucket_by_tag_00787([p]) == {"a": ["s1"]}
