"""Tests for catalog_01651."""

import pytest

from cartservice.generated.catalog_01651 import (
    Product_01651,
    bucket_by_tag_01651,
    is_valid_sku_01651,
    price_with_tax_01651,
)


def test_price_with_tax_01651():
    assert price_with_tax_01651(1000, 500) == 1050


def test_price_with_tax_negative_01651():
    with pytest.raises(ValueError):
        price_with_tax_01651(1000, -1)


def test_is_valid_sku_01651():
    assert is_valid_sku_01651("abc123")
    assert not is_valid_sku_01651("")


def test_bucket_by_tag_01651():
    p = Product_01651("s1", 100, ["a"])
    assert bucket_by_tag_01651([p]) == {"a": ["s1"]}
