"""Tests for catalog_00149."""

import pytest

from cartservice.generated.catalog_00149 import (
    Product_00149,
    bucket_by_tag_00149,
    is_valid_sku_00149,
    price_with_tax_00149,
)


def test_price_with_tax_00149():
    assert price_with_tax_00149(1000, 500) == 1050


def test_price_with_tax_negative_00149():
    with pytest.raises(ValueError):
        price_with_tax_00149(1000, -1)


def test_is_valid_sku_00149():
    assert is_valid_sku_00149("abc123")
    assert not is_valid_sku_00149("")


def test_bucket_by_tag_00149():
    p = Product_00149("s1", 100, ["a"])
    assert bucket_by_tag_00149([p]) == {"a": ["s1"]}
