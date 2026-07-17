"""Tests for catalog_00207."""

import pytest

from cartservice.generated.catalog_00207 import (
    Product_00207,
    bucket_by_tag_00207,
    is_valid_sku_00207,
    price_with_tax_00207,
)


def test_price_with_tax_00207():
    assert price_with_tax_00207(1000, 500) == 1050


def test_price_with_tax_negative_00207():
    with pytest.raises(ValueError):
        price_with_tax_00207(1000, -1)


def test_is_valid_sku_00207():
    assert is_valid_sku_00207("abc123")
    assert not is_valid_sku_00207("")


def test_bucket_by_tag_00207():
    p = Product_00207("s1", 100, ["a"])
    assert bucket_by_tag_00207([p]) == {"a": ["s1"]}
