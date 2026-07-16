"""Tests for catalog_01042."""

import pytest

from cartservice.generated.catalog_01042 import (
    Product_01042,
    bucket_by_tag_01042,
    is_valid_sku_01042,
    price_with_tax_01042,
)


def test_price_with_tax_01042():
    assert price_with_tax_01042(1000, 500) == 1050


def test_price_with_tax_negative_01042():
    with pytest.raises(ValueError):
        price_with_tax_01042(1000, -1)


def test_is_valid_sku_01042():
    assert is_valid_sku_01042("abc123")
    assert not is_valid_sku_01042("")


def test_bucket_by_tag_01042():
    p = Product_01042("s1", 100, ["a"])
    assert bucket_by_tag_01042([p]) == {"a": ["s1"]}
