"""Tests for catalog_00894."""

import pytest

from cartservice.generated.catalog_00894 import (
    Product_00894,
    bucket_by_tag_00894,
    is_valid_sku_00894,
    price_with_tax_00894,
)


def test_price_with_tax_00894():
    assert price_with_tax_00894(1000, 500) == 1050


def test_price_with_tax_negative_00894():
    with pytest.raises(ValueError):
        price_with_tax_00894(1000, -1)


def test_is_valid_sku_00894():
    assert is_valid_sku_00894("abc123")
    assert not is_valid_sku_00894("")


def test_bucket_by_tag_00894():
    p = Product_00894("s1", 100, ["a"])
    assert bucket_by_tag_00894([p]) == {"a": ["s1"]}
