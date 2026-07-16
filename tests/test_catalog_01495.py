"""Tests for catalog_01495."""

import pytest

from cartservice.generated.catalog_01495 import (
    Product_01495,
    bucket_by_tag_01495,
    is_valid_sku_01495,
    price_with_tax_01495,
)


def test_price_with_tax_01495():
    assert price_with_tax_01495(1000, 500) == 1050


def test_price_with_tax_negative_01495():
    with pytest.raises(ValueError):
        price_with_tax_01495(1000, -1)


def test_is_valid_sku_01495():
    assert is_valid_sku_01495("abc123")
    assert not is_valid_sku_01495("")


def test_bucket_by_tag_01495():
    p = Product_01495("s1", 100, ["a"])
    assert bucket_by_tag_01495([p]) == {"a": ["s1"]}
