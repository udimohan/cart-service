"""Tests for catalog_00108."""

import pytest

from cartservice.generated.catalog_00108 import (
    Product_00108,
    bucket_by_tag_00108,
    is_valid_sku_00108,
    price_with_tax_00108,
)


def test_price_with_tax_00108():
    assert price_with_tax_00108(1000, 500) == 1050


def test_price_with_tax_negative_00108():
    with pytest.raises(ValueError):
        price_with_tax_00108(1000, -1)


def test_is_valid_sku_00108():
    assert is_valid_sku_00108("abc123")
    assert not is_valid_sku_00108("")


def test_bucket_by_tag_00108():
    p = Product_00108("s1", 100, ["a"])
    assert bucket_by_tag_00108([p]) == {"a": ["s1"]}
