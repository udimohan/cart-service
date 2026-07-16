"""Tests for catalog_00995."""

import pytest

from cartservice.generated.catalog_00995 import (
    Product_00995,
    bucket_by_tag_00995,
    is_valid_sku_00995,
    price_with_tax_00995,
)


def test_price_with_tax_00995():
    assert price_with_tax_00995(1000, 500) == 1050


def test_price_with_tax_negative_00995():
    with pytest.raises(ValueError):
        price_with_tax_00995(1000, -1)


def test_is_valid_sku_00995():
    assert is_valid_sku_00995("abc123")
    assert not is_valid_sku_00995("")


def test_bucket_by_tag_00995():
    p = Product_00995("s1", 100, ["a"])
    assert bucket_by_tag_00995([p]) == {"a": ["s1"]}
