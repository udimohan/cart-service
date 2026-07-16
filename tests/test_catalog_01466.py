"""Tests for catalog_01466."""

import pytest

from cartservice.generated.catalog_01466 import (
    Product_01466,
    bucket_by_tag_01466,
    is_valid_sku_01466,
    price_with_tax_01466,
)


def test_price_with_tax_01466():
    assert price_with_tax_01466(1000, 500) == 1050


def test_price_with_tax_negative_01466():
    with pytest.raises(ValueError):
        price_with_tax_01466(1000, -1)


def test_is_valid_sku_01466():
    assert is_valid_sku_01466("abc123")
    assert not is_valid_sku_01466("")


def test_bucket_by_tag_01466():
    p = Product_01466("s1", 100, ["a"])
    assert bucket_by_tag_01466([p]) == {"a": ["s1"]}
