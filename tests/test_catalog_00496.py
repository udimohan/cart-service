"""Tests for catalog_00496."""

import pytest

from cartservice.generated.catalog_00496 import (
    Product_00496,
    bucket_by_tag_00496,
    is_valid_sku_00496,
    price_with_tax_00496,
)


def test_price_with_tax_00496():
    assert price_with_tax_00496(1000, 500) == 1050


def test_price_with_tax_negative_00496():
    with pytest.raises(ValueError):
        price_with_tax_00496(1000, -1)


def test_is_valid_sku_00496():
    assert is_valid_sku_00496("abc123")
    assert not is_valid_sku_00496("")


def test_bucket_by_tag_00496():
    p = Product_00496("s1", 100, ["a"])
    assert bucket_by_tag_00496([p]) == {"a": ["s1"]}
