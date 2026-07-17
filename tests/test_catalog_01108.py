"""Tests for catalog_01108."""

import pytest

from cartservice.generated.catalog_01108 import (
    Product_01108,
    bucket_by_tag_01108,
    is_valid_sku_01108,
    price_with_tax_01108,
)


def test_price_with_tax_01108():
    assert price_with_tax_01108(1000, 500) == 1050


def test_price_with_tax_negative_01108():
    with pytest.raises(ValueError):
        price_with_tax_01108(1000, -1)


def test_is_valid_sku_01108():
    assert is_valid_sku_01108("abc123")
    assert not is_valid_sku_01108("")


def test_bucket_by_tag_01108():
    p = Product_01108("s1", 100, ["a"])
    assert bucket_by_tag_01108([p]) == {"a": ["s1"]}
