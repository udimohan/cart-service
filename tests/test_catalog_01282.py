"""Tests for catalog_01282."""

import pytest

from cartservice.generated.catalog_01282 import (
    Product_01282,
    bucket_by_tag_01282,
    is_valid_sku_01282,
    price_with_tax_01282,
)


def test_price_with_tax_01282():
    assert price_with_tax_01282(1000, 500) == 1050


def test_price_with_tax_negative_01282():
    with pytest.raises(ValueError):
        price_with_tax_01282(1000, -1)


def test_is_valid_sku_01282():
    assert is_valid_sku_01282("abc123")
    assert not is_valid_sku_01282("")


def test_bucket_by_tag_01282():
    p = Product_01282("s1", 100, ["a"])
    assert bucket_by_tag_01282([p]) == {"a": ["s1"]}
