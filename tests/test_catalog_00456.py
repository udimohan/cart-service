"""Tests for catalog_00456."""

import pytest

from cartservice.generated.catalog_00456 import (
    Product_00456,
    bucket_by_tag_00456,
    is_valid_sku_00456,
    price_with_tax_00456,
)


def test_price_with_tax_00456():
    assert price_with_tax_00456(1000, 500) == 1050


def test_price_with_tax_negative_00456():
    with pytest.raises(ValueError):
        price_with_tax_00456(1000, -1)


def test_is_valid_sku_00456():
    assert is_valid_sku_00456("abc123")
    assert not is_valid_sku_00456("")


def test_bucket_by_tag_00456():
    p = Product_00456("s1", 100, ["a"])
    assert bucket_by_tag_00456([p]) == {"a": ["s1"]}
