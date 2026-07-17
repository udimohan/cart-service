"""Tests for catalog_00495."""

import pytest

from cartservice.generated.catalog_00495 import (
    Product_00495,
    bucket_by_tag_00495,
    is_valid_sku_00495,
    price_with_tax_00495,
)


def test_price_with_tax_00495():
    assert price_with_tax_00495(1000, 500) == 1050


def test_price_with_tax_negative_00495():
    with pytest.raises(ValueError):
        price_with_tax_00495(1000, -1)


def test_is_valid_sku_00495():
    assert is_valid_sku_00495("abc123")
    assert not is_valid_sku_00495("")


def test_bucket_by_tag_00495():
    p = Product_00495("s1", 100, ["a"])
    assert bucket_by_tag_00495([p]) == {"a": ["s1"]}
