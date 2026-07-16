"""Tests for catalog_00599."""

import pytest

from cartservice.generated.catalog_00599 import (
    Product_00599,
    bucket_by_tag_00599,
    is_valid_sku_00599,
    price_with_tax_00599,
)


def test_price_with_tax_00599():
    assert price_with_tax_00599(1000, 500) == 1050


def test_price_with_tax_negative_00599():
    with pytest.raises(ValueError):
        price_with_tax_00599(1000, -1)


def test_is_valid_sku_00599():
    assert is_valid_sku_00599("abc123")
    assert not is_valid_sku_00599("")


def test_bucket_by_tag_00599():
    p = Product_00599("s1", 100, ["a"])
    assert bucket_by_tag_00599([p]) == {"a": ["s1"]}
