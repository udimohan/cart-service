"""Tests for catalog_01399."""

import pytest

from cartservice.generated.catalog_01399 import (
    Product_01399,
    bucket_by_tag_01399,
    is_valid_sku_01399,
    price_with_tax_01399,
)


def test_price_with_tax_01399():
    assert price_with_tax_01399(1000, 500) == 1050


def test_price_with_tax_negative_01399():
    with pytest.raises(ValueError):
        price_with_tax_01399(1000, -1)


def test_is_valid_sku_01399():
    assert is_valid_sku_01399("abc123")
    assert not is_valid_sku_01399("")


def test_bucket_by_tag_01399():
    p = Product_01399("s1", 100, ["a"])
    assert bucket_by_tag_01399([p]) == {"a": ["s1"]}
