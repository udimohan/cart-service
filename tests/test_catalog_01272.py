"""Tests for catalog_01272."""

import pytest

from cartservice.generated.catalog_01272 import (
    Product_01272,
    bucket_by_tag_01272,
    is_valid_sku_01272,
    price_with_tax_01272,
)


def test_price_with_tax_01272():
    assert price_with_tax_01272(1000, 500) == 1050


def test_price_with_tax_negative_01272():
    with pytest.raises(ValueError):
        price_with_tax_01272(1000, -1)


def test_is_valid_sku_01272():
    assert is_valid_sku_01272("abc123")
    assert not is_valid_sku_01272("")


def test_bucket_by_tag_01272():
    p = Product_01272("s1", 100, ["a"])
    assert bucket_by_tag_01272([p]) == {"a": ["s1"]}
