"""Tests for catalog_00519."""

import pytest

from cartservice.generated.catalog_00519 import (
    Product_00519,
    bucket_by_tag_00519,
    is_valid_sku_00519,
    price_with_tax_00519,
)


def test_price_with_tax_00519():
    assert price_with_tax_00519(1000, 500) == 1050


def test_price_with_tax_negative_00519():
    with pytest.raises(ValueError):
        price_with_tax_00519(1000, -1)


def test_is_valid_sku_00519():
    assert is_valid_sku_00519("abc123")
    assert not is_valid_sku_00519("")


def test_bucket_by_tag_00519():
    p = Product_00519("s1", 100, ["a"])
    assert bucket_by_tag_00519([p]) == {"a": ["s1"]}
