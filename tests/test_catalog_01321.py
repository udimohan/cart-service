"""Tests for catalog_01321."""

import pytest

from cartservice.generated.catalog_01321 import (
    Product_01321,
    bucket_by_tag_01321,
    is_valid_sku_01321,
    price_with_tax_01321,
)


def test_price_with_tax_01321():
    assert price_with_tax_01321(1000, 500) == 1050


def test_price_with_tax_negative_01321():
    with pytest.raises(ValueError):
        price_with_tax_01321(1000, -1)


def test_is_valid_sku_01321():
    assert is_valid_sku_01321("abc123")
    assert not is_valid_sku_01321("")


def test_bucket_by_tag_01321():
    p = Product_01321("s1", 100, ["a"])
    assert bucket_by_tag_01321([p]) == {"a": ["s1"]}
