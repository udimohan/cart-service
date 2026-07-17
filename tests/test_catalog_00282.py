"""Tests for catalog_00282."""

import pytest

from cartservice.generated.catalog_00282 import (
    Product_00282,
    bucket_by_tag_00282,
    is_valid_sku_00282,
    price_with_tax_00282,
)


def test_price_with_tax_00282():
    assert price_with_tax_00282(1000, 500) == 1050


def test_price_with_tax_negative_00282():
    with pytest.raises(ValueError):
        price_with_tax_00282(1000, -1)


def test_is_valid_sku_00282():
    assert is_valid_sku_00282("abc123")
    assert not is_valid_sku_00282("")


def test_bucket_by_tag_00282():
    p = Product_00282("s1", 100, ["a"])
    assert bucket_by_tag_00282([p]) == {"a": ["s1"]}
