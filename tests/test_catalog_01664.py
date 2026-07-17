"""Tests for catalog_01664."""

import pytest

from cartservice.generated.catalog_01664 import (
    Product_01664,
    bucket_by_tag_01664,
    is_valid_sku_01664,
    price_with_tax_01664,
)


def test_price_with_tax_01664():
    assert price_with_tax_01664(1000, 500) == 1050


def test_price_with_tax_negative_01664():
    with pytest.raises(ValueError):
        price_with_tax_01664(1000, -1)


def test_is_valid_sku_01664():
    assert is_valid_sku_01664("abc123")
    assert not is_valid_sku_01664("")


def test_bucket_by_tag_01664():
    p = Product_01664("s1", 100, ["a"])
    assert bucket_by_tag_01664([p]) == {"a": ["s1"]}
