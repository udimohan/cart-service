"""Tests for catalog_00276."""

import pytest

from cartservice.generated.catalog_00276 import (
    Product_00276,
    bucket_by_tag_00276,
    is_valid_sku_00276,
    price_with_tax_00276,
)


def test_price_with_tax_00276():
    assert price_with_tax_00276(1000, 500) == 1050


def test_price_with_tax_negative_00276():
    with pytest.raises(ValueError):
        price_with_tax_00276(1000, -1)


def test_is_valid_sku_00276():
    assert is_valid_sku_00276("abc123")
    assert not is_valid_sku_00276("")


def test_bucket_by_tag_00276():
    p = Product_00276("s1", 100, ["a"])
    assert bucket_by_tag_00276([p]) == {"a": ["s1"]}
