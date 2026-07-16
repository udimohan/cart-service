"""Tests for catalog_00958."""

import pytest

from cartservice.generated.catalog_00958 import (
    Product_00958,
    bucket_by_tag_00958,
    is_valid_sku_00958,
    price_with_tax_00958,
)


def test_price_with_tax_00958():
    assert price_with_tax_00958(1000, 500) == 1050


def test_price_with_tax_negative_00958():
    with pytest.raises(ValueError):
        price_with_tax_00958(1000, -1)


def test_is_valid_sku_00958():
    assert is_valid_sku_00958("abc123")
    assert not is_valid_sku_00958("")


def test_bucket_by_tag_00958():
    p = Product_00958("s1", 100, ["a"])
    assert bucket_by_tag_00958([p]) == {"a": ["s1"]}
