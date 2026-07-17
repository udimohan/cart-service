"""Tests for catalog_01315."""

import pytest

from cartservice.generated.catalog_01315 import (
    Product_01315,
    bucket_by_tag_01315,
    is_valid_sku_01315,
    price_with_tax_01315,
)


def test_price_with_tax_01315():
    assert price_with_tax_01315(1000, 500) == 1050


def test_price_with_tax_negative_01315():
    with pytest.raises(ValueError):
        price_with_tax_01315(1000, -1)


def test_is_valid_sku_01315():
    assert is_valid_sku_01315("abc123")
    assert not is_valid_sku_01315("")


def test_bucket_by_tag_01315():
    p = Product_01315("s1", 100, ["a"])
    assert bucket_by_tag_01315([p]) == {"a": ["s1"]}
