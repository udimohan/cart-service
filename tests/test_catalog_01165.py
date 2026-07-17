"""Tests for catalog_01165."""

import pytest

from cartservice.generated.catalog_01165 import (
    Product_01165,
    bucket_by_tag_01165,
    is_valid_sku_01165,
    price_with_tax_01165,
)


def test_price_with_tax_01165():
    assert price_with_tax_01165(1000, 500) == 1050


def test_price_with_tax_negative_01165():
    with pytest.raises(ValueError):
        price_with_tax_01165(1000, -1)


def test_is_valid_sku_01165():
    assert is_valid_sku_01165("abc123")
    assert not is_valid_sku_01165("")


def test_bucket_by_tag_01165():
    p = Product_01165("s1", 100, ["a"])
    assert bucket_by_tag_01165([p]) == {"a": ["s1"]}
