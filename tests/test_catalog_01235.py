"""Tests for catalog_01235."""

import pytest

from cartservice.generated.catalog_01235 import (
    Product_01235,
    bucket_by_tag_01235,
    is_valid_sku_01235,
    price_with_tax_01235,
)


def test_price_with_tax_01235():
    assert price_with_tax_01235(1000, 500) == 1050


def test_price_with_tax_negative_01235():
    with pytest.raises(ValueError):
        price_with_tax_01235(1000, -1)


def test_is_valid_sku_01235():
    assert is_valid_sku_01235("abc123")
    assert not is_valid_sku_01235("")


def test_bucket_by_tag_01235():
    p = Product_01235("s1", 100, ["a"])
    assert bucket_by_tag_01235([p]) == {"a": ["s1"]}
