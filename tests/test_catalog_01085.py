"""Tests for catalog_01085."""

import pytest

from cartservice.generated.catalog_01085 import (
    Product_01085,
    bucket_by_tag_01085,
    is_valid_sku_01085,
    price_with_tax_01085,
)


def test_price_with_tax_01085():
    assert price_with_tax_01085(1000, 500) == 1050


def test_price_with_tax_negative_01085():
    with pytest.raises(ValueError):
        price_with_tax_01085(1000, -1)


def test_is_valid_sku_01085():
    assert is_valid_sku_01085("abc123")
    assert not is_valid_sku_01085("")


def test_bucket_by_tag_01085():
    p = Product_01085("s1", 100, ["a"])
    assert bucket_by_tag_01085([p]) == {"a": ["s1"]}
