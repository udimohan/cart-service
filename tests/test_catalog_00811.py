"""Tests for catalog_00811."""

import pytest

from cartservice.generated.catalog_00811 import (
    Product_00811,
    bucket_by_tag_00811,
    is_valid_sku_00811,
    price_with_tax_00811,
)


def test_price_with_tax_00811():
    assert price_with_tax_00811(1000, 500) == 1050


def test_price_with_tax_negative_00811():
    with pytest.raises(ValueError):
        price_with_tax_00811(1000, -1)


def test_is_valid_sku_00811():
    assert is_valid_sku_00811("abc123")
    assert not is_valid_sku_00811("")


def test_bucket_by_tag_00811():
    p = Product_00811("s1", 100, ["a"])
    assert bucket_by_tag_00811([p]) == {"a": ["s1"]}
