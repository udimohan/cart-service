"""Tests for catalog_01630."""

import pytest

from cartservice.generated.catalog_01630 import (
    Product_01630,
    bucket_by_tag_01630,
    is_valid_sku_01630,
    price_with_tax_01630,
)


def test_price_with_tax_01630():
    assert price_with_tax_01630(1000, 500) == 1050


def test_price_with_tax_negative_01630():
    with pytest.raises(ValueError):
        price_with_tax_01630(1000, -1)


def test_is_valid_sku_01630():
    assert is_valid_sku_01630("abc123")
    assert not is_valid_sku_01630("")


def test_bucket_by_tag_01630():
    p = Product_01630("s1", 100, ["a"])
    assert bucket_by_tag_01630([p]) == {"a": ["s1"]}
