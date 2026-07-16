"""Tests for catalog_00861."""

import pytest

from cartservice.generated.catalog_00861 import (
    Product_00861,
    bucket_by_tag_00861,
    is_valid_sku_00861,
    price_with_tax_00861,
)


def test_price_with_tax_00861():
    assert price_with_tax_00861(1000, 500) == 1050


def test_price_with_tax_negative_00861():
    with pytest.raises(ValueError):
        price_with_tax_00861(1000, -1)


def test_is_valid_sku_00861():
    assert is_valid_sku_00861("abc123")
    assert not is_valid_sku_00861("")


def test_bucket_by_tag_00861():
    p = Product_00861("s1", 100, ["a"])
    assert bucket_by_tag_00861([p]) == {"a": ["s1"]}
